module Day02 where
import Data.List (groupBy,sort)
import Data.List.Split
import Data.Char (ord)
import Utils


points :: Char -> Char -> Int
--points a b = ((ord a + ord b) `mod` 3) * 3

points 'A' 'X' = 3
-- 0 0 = 3
points 'A' 'Y' = 6
-- 0 1 = 6

points 'A' 'Z' = 0
-- 0 2 = 0

points 'B' 'X' = 0
-- 1 0 = 0
points 'B' 'Y' = 3
-- 1 1 = 3
points 'B' 'Z' = 6
--1 2 = 6

points 'C' 'X' = 6
--2 0 = 6
points 'C' 'Y' = 0
-- 2 1 = 0
points 'C' 'Z' = 3
-- 2 2 = 3

point :: Char -> Int
point a = ord a - ord 'X' +1

--day2Part1 :: IO ()
day2Part1 = do
    inp <- readFile "inputs/Day2.in"

    let ans = [points a b + point b | x <- map words $ lines inp, let [a,b] = map head $ take 2 x]

    print $ sum ans

--day2Part2 :: IO ()
day2Part2 = undefined

--day2 :: IO ()
day2 = solveDay day2Part1 day2Part2 2