import { test, expect } from '@playwright/test';

test('navigateToForumsPage', async ({ page }) => {
  await page.goto('https://www.selenium.dev/');
  await page.hover('text=Community');
  await page.click('text=Forums');
  const newPage = await page.waitForEvent('page');
  await newPage.waitForLoadState('networkidle');
  expect(newPage.url()).toBe('https://www.selenium.dev/forums/');
});

test('verifyForumsHeaderPresent', async ({ page }) => {
  await page.goto('https://www.selenium.dev/forums/');
  const forumsHeader = await page.waitForSelector('text=Forums');
  expect(forumsHeader).toBeTruthy();
});

test('clickNextPage', async ({ page }) => {
  await page.goto('https://www.selenium.dev/forums/');
  const pagination = await page.waitForSelector('.pagination');
  const pages = await pagination.querySelectorAll('a');
  for (let i = 1; i < pages.length; i++) {
    await pages[i].click();
    await page.waitForLoadState('networkidle');
    expect(page.url()).toContain(`/forums/page/${i + 1}`);
  }
});

test('verifyForumSearch', async ({ page }) => {
  await page.goto('https://www.selenium.dev/forums/');
  await page.fill('input[type="search"]', 'error');
  await page.press('input[type="search"]', 'Enter');
  await page.waitForLoadState('networkidle');
  const searchResults = await page.waitForSelector('.search-results');
  expect(searchResults).toBeTruthy();
});