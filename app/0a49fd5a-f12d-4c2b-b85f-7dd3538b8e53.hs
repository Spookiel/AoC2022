module Day05 where
import Data.List (groupBy,sort)
import Data.List.Index (indexed)
import Data.List.Split (splitOn, chunksOf)
import Data.Maybe
import Text.Read
import Utils

type Stack = String
type Wharf = [Stack]
type Instruction = [Int]


parseRow :: String -> [(Int, Char)]
parseRow  s = filter (\(a,b) -> b /= ' ') (map (\(a,b) -> (a, head b)) (indexed $ chunksOf 4 (tail s)))


buildNewStack:: Stack -> (Int, Char) -> Stack
buildNewStack s (tind, nchar) = nchar:s


buildRow :: Wharf -> [(Int, Char)] -> Wharf
buildRow wharf sframe = [fromMaybe (wharf!!i) (lookup i changed)| i <- [0..(length wharf -1 )]] where
    changed = [(tind, buildNewStack (wharf!!tind) (tind, nchar))| (tind, nchar) <- sframe]

-- Replaces stack at index with the new stack
replaceStack :: Wharf -> Int -> Stack -> Wharf
replaceStack wharf tind nstack = [if(i==tind) then nstack else j|(i, j) <- indexed wharf]

buildStacks :: [[(Int, Char)]] -> Wharf
buildStacks prows = map reverse $ foldl buildRow [[] | i <- [0..9]] prows


moveN :: Int -> Stack -> Stack -> (Stack, Stack)
moveN n s1 s2 = (drop n s1, added ++ s2) where added = take n s1

parseLine :: String -> [Int]
parseLine line = mapMaybe readMaybe $ words line

applyInst1 :: Wharf -> Instruction -> Wharf
applyInst1 wharf [0 ,b,c] = wharf
applyInst1 wharf [n,b,c] = applyInst1 nwharf2 [n-1,b,c] where
    ostack1 = wharf!!(b-1)
    ostack2 = wharf!!(c-1)
    (nstack1, nstack2) = moveN 1 ostack1 ostack2
    nwharf1 = replaceStack wharf (b-1) nstack1
    nwharf2 = replaceStack nwharf1 (c-1) nstack2

day5Part1 = do
    inp <- readFile "inputs/Day5.in"
    let [a,b] = splitOn "\n\n" inp
    let stacks = buildStacks (init (map parseRow (lines a)))
    let insts = map parseLine $ lines b
    print insts
    let finished = foldl applyInst1 stacks insts
    --let answer = mapMaybe safeHead finished
    print finished

-- let stacks = ["ABC", "", ""]
-- let insts1 = [[3,1,3]]

day5Part2 = undefined

day5 = solveDay day5Part1 day5Part2 5