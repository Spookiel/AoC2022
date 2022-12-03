module Day01 where
import Data.List (groupBy,sort)
import Data.List.Split
import Utils



getGroups inp = [sum $ map read (splitOn "\n" i) | i <- splitOn "\n\n" inp]


day1Part1 = do
    inp <- readFile "inputs/Day1.in"
    print $ maximum $ getGroups inp

    
day1Part2 = do
    inp <- readFile "inputs/Day1.in"
    let groups = getGroups inp

    print $ sum  $ take 3 (reverse $ sort groups)

day1 = solveDay day1Part1 day1Part2 1


