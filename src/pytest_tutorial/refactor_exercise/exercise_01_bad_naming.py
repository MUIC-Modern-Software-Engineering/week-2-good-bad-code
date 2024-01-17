# this function is meant to calculate tax a coporate needs to pay.
# The coporate get tax on
# 1. Its profit. Which is revenue - claimable expense
# 2. However some expense is forbidden and can't be claimed as expense. So claimable expense = real expense - forbidden_expense
# 3. The government does give out some incentive for certain kind of expense 
#    (ex: paying intern for Coop) those kind of expense can be claimed 1.5 times the actual expense
#    this means some of those claimable expense will need to be increase by 0.5xexpense incentivize by gov.
# 4. Again the government does allow the loss carry from last year to be claimed as deductible expense as well.
# 5. After all those deduction mentioned above the company gets taxed at flat 20% rate.
#    That about is the amount of tax we are supposed to pay the government.
# 6. But, over the years the company has
#    been paying the government some tax as well. So tax that the company need to pay at the end of year in addition to what
#    has been paid is amount you are supposed to pay - tax you paid in advance.
# 7. A lovely programmer who has quite the job and now you have to take over his code wrote the following:
# 8. tasks for you... 1) is it correct? 2) I know you hate it. Find the bug fix it. 3) make it more readable.
def ct(r, e, f, i, ir, l, t, a):
  c = e + f + i*ir + l
  tt = (r + c)*t
  return tt-a
