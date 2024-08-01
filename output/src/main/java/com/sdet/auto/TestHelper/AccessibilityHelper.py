```
import axeCore from 'playwright-axe';

export class AccessibilityHelper {
  static async basicAccessibilityCheck(testAssert) {
    const results = await axeCore.run(page);
    const violations = results.violations;

    if (violations.length === 0) {
      IoLibrary.writeLine('PASS: basicAccessibilityCheck | No violations found.');
    } else {
      await axeCore.writeResults('FAIL:'+ IoLibrary.getTestName(), results);
      testAssert.setPass(false);
      IoLibrary.writeLine('FAIL:'+ IoLibrary.getTestName() +'' + AXE.report(violations));
    }
  }
}
```