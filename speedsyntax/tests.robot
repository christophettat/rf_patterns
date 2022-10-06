*** Test cases ***
My Test 1
  sleep  1
  Log  I'm alive
  log  I'm in good health
  KW1
  KW2 has "MAny" embedded arguments
  [Teardown]    log  teardown


My Test 2
  sleep  3
  Log  I'm alive
  log  I'm in good health
  KW1 

My Test 3
  KW2 has "MAny" embedded arguments
  sleep  3
  Log many  I'm alive
  log  I'm in good health
  KW1 


*** Keywords ***
KW1
    log  KW1

KW2 has ${arg} embedded arguments
    log  ${arg}
    KW3 

KW3
    log  KW3
