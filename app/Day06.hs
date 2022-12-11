module Day06 where
import Data.List (groupBy,sort, nub)
import Data.List.Index (indexed)
import Data.List.Split (splitOn, chunksOf)
import Data.Maybe
import Text.Read
import Utils



solve :: String -> Int -> Int
solve s chunkSize = solveHelper s 0 where 
    solveHelper :: String -> Int -> Int
    solveHelper s@(c:cs) ind
        | length s < chunkSize = -1
        | uni == chunkSize = ind+chunkSize
        | otherwise = solveHelper cs (ind+1)
        where 
            fblock = take chunkSize s
            uni = length $ nub fblock


day6Part1 = do

    inp <-  readFile "inputs/Day6.in"

    print $ solve inp 4




day6Part2 = do
    inp <- readFile "inputs/Day6.in"
    print $ solve inp 14



day6 = solveDay day6Part1 day6Part2 6