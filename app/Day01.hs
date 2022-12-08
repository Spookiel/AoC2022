module Day01 where
import Data.List (groupBy,sort)
import Data.List.Split
import Utils



getGroups :: (Num a, Read a) => [Char] -> [a]
getGroups inp = [sum $ map read (splitOn "\n" i) | i <- splitOn "\n\n" inp]


day1Part1 = do
    inp <- readFile "inputs/Day1.in"
    let part1 = maximum . getGroups
    print $ part1 inp

    
day1Part2 = do
    inp <- readFile "inputs/Day1.in"
    let part2 = sum . 
             take 3 . 
            reverse . 
               sort . getGroups

    print $ part2 inp

day1 = solveDay day1Part1 day1Part2 1


