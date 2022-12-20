module Day05 where
import Data.List (groupBy,sort)
import Data.List.Index (indexed)
import Data.List.Split (splitOn, chunksOf)
import Data.IntMap (IntMap, (!), adjust, elems, insertWith)
import Control.Monad.State
import qualified Data.IntMap as IM
import Data.Maybe
import Debug.Trace
import Utils
import Text.Read (readMaybe)

-- type Stack = String
-- type Wharf = [Stack]
-- type Stacks = IntMap Stack

type Crate  = Char
type Stack  = [Char]
type Stacks = IntMap Stack
type Procedure = State Stacks


type Instruction = [Int]


parseRow :: String -> [(Int, Char)]
parseRow  s = filter (\(a,b) -> b /= ' ') (map (\(a,b) -> (a, head b)) (indexed $ chunksOf 4 (tail s)))

buildIMRowSingle :: Stacks -> (Int, Char) -> Stacks
buildIMRowSingle swharf (snum, schar) = insertWith (flip (++)) (snum+1) [schar] swharf

buildCompleteRow :: Stacks -> [(Int, Char)] -> Stacks
buildCompleteRow = foldl buildIMRowSingle

parseLine :: String -> [Int]
parseLine line = mapMaybe readMaybe $ words line

-- pop :: Int -> Procedure Char
-- pop i = do
--     cstate <- get
--     (c:cs) <- cstate ! i
--     nstate <- adjust tail i cstate
--     put nstate
--     pure c


push :: Int -> Char -> Procedure ()
push i c = do
    cstate <- get
    let nstate = adjust (c:) i cstate
    put nstate

pop :: Int -> Procedure Char
pop i = do
    cstate <- get
    let (c:cs) = cstate ! i
    let nstate = adjust tail i cstate
    put nstate
    pure c

execute9000 :: [Int] -> Procedure ()
execute9000 [n,a,b] = do
    ostate <- get
    let ostates = replicate n ostate
    







parse5 = do
    inp <- readFile "inputs/Day5.in"
    let [a,b] = splitOn "\n\n" inp
    let sinfo = init (map parseRow (lines a))
    let stacks = foldl buildCompleteRow IM.empty sinfo
    let insts = map parseLine $ lines b
    return (stacks, insts)

getFirsts :: [String] -> String
getFirsts = mapMaybe safeHead 


day5Part1 = do
    (stacks, insts) <- parse5
    let answer = foldl execute9000 stacks insts
    print $ getFirsts $  elems answer

day5Part2 = do
    (stacks, insts) <- parse5
    let answer = foldl execute9001 stacks insts
    print $ getFirsts $ elems answer

day5 = solveDay day5Part1 day5Part2 5