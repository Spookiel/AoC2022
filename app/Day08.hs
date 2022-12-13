module Day08 where
import Data.List
import Data.Char
import Utils
import Debug.Trace


checkLstLR row = reverse  $ go row (-1) [] where

    go :: [Int] -> Int -> [Int] -> [Int]

    go [] _ acc = acc
    go (v:vs) msf acc
        | v > msf = go vs v (1:acc)
        | otherwise = go vs msf (0:acc)

merge :: [Int] -> [Int] -> [Int]
merge = zipWith comp  where
    comp 0 1 = 1
    comp 1 0 = 1
    comp 1 1 = 1
    comp 0 0 = 0


getRow :: [[Int]] -> Int -> [Int]
getRow lst r = lst !! r

getCol :: [[Int]] -> Int -> [Int]
getCol lst c = [row!!c | row <- lst]


checkLst lst = merge (checkLstLR lst) (reverse $ checkLstLR $ reverse lst)


checkRows = map checkLst 
checkCols =  transpose . map checkLst  . transpose

checkGrid grid = sum [sum $ merge a b | (a,b) <- zip (checkRows grid) (checkCols grid)]

tlst :: [[Int]]
tlst = [[1,2,3,3,7], 
        [6,2,4,1,5], 
        [7,8,9,3,5]]


countSee [] val = 0
countSee (r:rs) val
    | r < val = 1 + countSee rs val
    | otherwise = 1

checkSee :: [[Int]] -> Int -> Int -> Int
checkSee lst row col  = product ls where
    (a,(it:b)) = splitAt col (getRow lst row)
    (c,(_:d)) = splitAt row (getCol lst col)
    
    v = lst!!row!!col
    ls = map (flip countSee v) [reverse a,b,reverse c,d]
    


day8Part1 = do
    inp <- readFile "inputs/Day8.in"



    let grid = [map digitToInt i |i <- lines inp]
    --let s = [1| row <- [0.. (length grid - 1)], col <- [0..(length grid - 1)], checkSee grid row col ]


    --print $ checkCols grid
    print $ checkGrid grid

day8Part2 = do
    inp <- readFile "inputs/Day8.in"



    let grid = [map digitToInt i |i <- lines inp]


    let s = maximum [checkSee grid row col | row <- [0.. (length grid - 1)], col <- [0..(length grid - 1)]]
    print s


day8 = solveDay day8Part1 day8Part2 8