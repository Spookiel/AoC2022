module Day08 where
import Data.Ix
import Utils



tlst = [[1,2,3], [4,5,6], [7,8,9]]

getRow :: [[Int]] -> Int -> [Int]
getRow lst r = lst !! r

getCol :: [[Int]] -> Int -> [Int]
getCol lst c = [row!!c | row <- lst]

checkSee :: [[Int]] -> Int -> Int -> Bool
checkSee lst row col  = flag where
    (a,(it:b)) = splitAt col (getRow lst row)
    (c,(_:d)) = splitAt row (getCol lst col)

    l = [a,b,c,d]
    flag = any null l || any (< it) (map maximum l)


readInt :: Char -> Int
readInt c = read [c]

day8Part1 = do
    inp <- readFile "inputs/Day8.in"



    let grid = [map readInt i |i <- lines inp]
    let s = [1| row <- [0.. (length grid - 1)], col <- [0..(length grid - 1)], checkSee grid row col ]


    print $ sum s

day8Part2 = do
    print "undone"


day8 = solveDay day8Part1 day8Part2 8