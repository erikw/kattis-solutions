import System.IO

iter   []   (t:ts) = False
iter   _     []    = True
iter (a:as) (t:ts) = iter as ts


main = do
    aah <- getLine
    targetaah <- getLine


    if iter aah targetaah then putStrLn "go" else putStrLn "no"

