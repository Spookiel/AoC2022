module Day02 where
import Data.List (groupBy,sort)
import Data.List.Split
import Data.Char (ord)
import Utils


toRSP :: Char -> Int
toRSP a 
    | a `elem` "ABC" = ord a - ord 'A'
    | otherwise = ord a - ord 'X'

points :: Char -> Char -> Int
points a b = case (toRSP a - toRSP b) `mod` 3 of
    0 -> 3
    1 -> 0
    2 -> 6


need :: Char -> Char -> Int
need a 'Y' = toRSP a + 1
need a 'X' = (toRSP a - 1) `mod` 3 + 1
need a 'Z' = (toRSP a + 1) `mod` 3 + 1

res :: Char -> Int
res 'Y' = 3
res 'Z' = 6
res 'X' = 0

--day2Part1 :: IO ()

parseDay2 s = [(a,b) |  x <- map words $ lines s, let [a,b] = map head $ take 2 x]

day2Part1 = do
    inp <- readFile "inputs/Day2.in"

    let ans = [points a b + toRSP b + 1| (a,b) <- parseDay2 inp]
    --print ans
    print $ sum ans

--day2Part2 :: IO ()
day2Part2 = do
    inp <- readFile "inputs/Day2.in"

    let ans = [res b + need a b| (a,b) <- parseDay2 inp]

    print $ sum ans

--day2 :: IO ()
day2 = solveDay day2Part1 day2Part2 2