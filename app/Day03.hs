module Day03 where
import Data.List (groupBy,sort)
import Data.List.Split (chunksOf)
import Data.Char (ord, toUpper)
import Utils

score :: String -> Int
score s 
    | c == toUpper c = ord c - 38
    | otherwise = ord c - 96
    where c = head s 

getUnion2 :: String -> String -> String
getUnion2 s1 s2 =  [x| x <- s1, x `elem` s2]

getUnion3 :: String -> String -> String -> String
getUnion3 s1 s2 s3 = getUnion2 s3 $ getUnion2 s1 s2

splitHalf :: String -> (String, String)
splitHalf s = splitAt req s where
    req = length s `div` 2

day3Part1 = do
    inp <- readFile "inputs/Day3.in"
    let ans = sum [score $ getUnion2 a b| (a,b) <- map splitHalf $ lines inp]
    print ans
day3Part2 = do
    inp <- readFile "inputs/Day3.in"
    let ans = sum [score $ getUnion3 a b c| [a,b,c] <- (chunksOf 3) $ lines inp]
    print ans

day3 = solveDay day3Part1 day3Part2 3