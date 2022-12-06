module Utils where
import Data.List (groupBy, sort)
import Data.List.Split (splitOn)




safeHead :: [a] -> Maybe a
safeHead [] = Nothing
safeHead (x:xs) = Just x

--splitDoubleNewLine :: String -> [String]
splitDoubleNewLine s =  filter (/=[""]) ans
    where
        ans =  groupBy func $ lines s

        func:: String -> String -> Bool
        func a b = a /= "" && b /= ""

splitOnCharAux :: Char -> String -> String -> [String]

splitOnChar:: Char -> String -> [String]
splitOnChar delim string  = splitOnCharAux delim string ""

splitOnCharAux delim "" acc = [reverse acc]
splitOnCharAux delim (x:xs) acc 
    | x == delim = reverse acc : splitOnCharAux delim xs []
    | otherwise = splitOnCharAux delim xs (x:acc)

solveDay p1 p2 dayNum= do
    putStrLn ("     DAY " ++ show dayNum ++ "     ")
    putStrLn "--------------"
    putStr  "part1: "
    p1
    putStr "part2: "
    p2
    putStrLn "--------------"
    