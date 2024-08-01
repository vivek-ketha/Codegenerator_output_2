import com.microsoft.playwright.*;
import java.util.List;

public class ForumsPage {
    
    Locator forumsHeader = page.locator(".c_Header-logoLink");
    Locator paginationBar = page.locator("#PagerBefore");
    Locator numberedPages = page.locator("a");
    Locator newResults = page.locator(".DataList.Discussions");
    Locator forumsSearchBar = page.locator("#Form_Search");
    Locator forumsSearchResults = page.locator("#search-results");
    
    Page page;
    
    public ForumsPage(Page page) {
        this.page = page;
    }
    
    public boolean isForumsHeaderPresent() {
        return page.waitForSelector(forumsHeader).isDisplayed();
    }
    
    public List<Element> getPagination() {
        return paginationBar.querySelectorAll(numberedPages);
    }
    
    public boolean isNextPageSuccessful() {
        return page.waitForSelector(newResults).isDisplayed();
    }
    
    public void searchForum(String text) {
        page.locator(forumsSearchBar).fill(text);
    }
    
    public void pressEnter() {
        page.keyboard().press("Enter");
    }
    
    public boolean isSearchSuccessful() {
        return page.waitForSelector(forumsSearchResults).isDisplayed();
    }
}