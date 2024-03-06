## Auction Testing Problem

| File        | Description |
|:------------|:------------|
| `auction.py` | Sample code code. May contain defects. |
| `test_auction.py` | Starter code for unit tests. |

## Assignment

1. Write tests for all the Auction requirements in the file `test_auction.py`. 
   - You can use unittest or pytest syntax for your tests.
   - The starter code uses unittest, but you can replace it with pytest if you prefer.
2. When you submit your test code to Github it will run your tests using 8 different Auction codes.  One code is correct and the other variations contain at least 1 violation of the auction rules.
3. Try to make your tests all PASS for the good Auction code, and at least one Failure for the others.
4. Analyze the output on Github Actions and try to identify the errors. Complete the table below.

Guidelines for tests:

- Write tests for how the code **should** behave based on the **specification**. 
- The sample Auction code (in repo) may contain errors.  Your auction tests should not assume the sample code is correct.
- Test behavior **not** attributes. You can test the values of *properties*.
- Any test that directly access attributes of Auction will be marked as incorrect.

## Running Your Tests

When you push code to Github, it will automatically run your tests
using a Github Action.  Click the **Actions** tab to view the results.

The Action will test your code using **8 different versions** of Auction.

1 version of Auction is correct. Your tests should **all pass**.

7 versions contain at least one defect. Some test(s) should **fail** or **error**.

If a test method fails on *all 8* versions of Auction, the test is probably incorrect.

## What to Submit

Push your code and your analysis of errors (table below) to Github classroom. 


## Error Analysis

Study the output of Github Actions.  For each auction variant where you detect an error, answer these questions in the table below:

1. Describe the nature of the defect.  What auction requirement was violated?
2. Which Auction method caused the error?
  - sometimes you may not be able to determine the faulty method

If your answer is too long to fit in the table, write a paragraph below & identify which Test Case you are describing.

If all tests pass, write "No defect found." in the table.


| Auction |  Your analysis of the defect                                       |
|:-------:|:-------------------------------------------------------------------|
| 1       |                                                                    |
| 2       |                                                                    |
| 3       |                                                                    |
| 4       |                                                                    |
| 5       |                                                                    |
| 6       |                                                                    |
| 7       |                                                                    |
| 8       |                                                                    |
