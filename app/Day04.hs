module Day04 where
import Data.List (groupBy,sort)
import Data.List.Split (splitOn)
import Utils

checkContains :: [Int] -> [Int] -> Bool
checkContains [a,b] [c,d]
    | a <= c = b >= d
    | c <= a = d >= b
checkOverlaps [a,b] [c,d]
    | a <= c = b >= c
    | otherwise = d >= a

parse4 = do
    inp <- readFile "inputs/Day4.in"
    let groups = [map (splitOn "-") x |x <-  map (splitOn ",") (lines inp)]
    let vals = [map (map (\x -> read x :: Int)) x| x <- groups]
    --print vals
    return vals

day4Part1 = do
    vals <- parse4
    print $ sum [1 | [xs,ys] <- vals, checkContains xs ys || checkContains ys xs]

day4Part2 = do
    vals <- parse4
    print $ sum [1 | [xs,ys] <- vals, checkOverlaps xs ys || checkOverlaps ys xs]



day4 = solveDay day4Part1 day4Part2 4