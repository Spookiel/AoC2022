module Day05 where
import Data.List (groupBy,sort)
import Data.List.Index (indexed)
import Data.List.Split (splitOn, chunksOf)
import Data.IntMap (IntMap, (!), adjust, elems, insertWith)
import qualified Data.IntMap as IM
import Data.Maybe
import Text.Read
import Debug.Trace
import Utils

type Stack = String
type Wharf = [Stack]
type FastWharf = IntMap Stack
type Instruction = [Int]


parseRow :: String -> [(Int, Char)]
parseRow  s = filter (\(a,b) -> b /= ' ') (map (\(a,b) -> (a, head b)) (indexed $ chunksOf 4 (tail s)))


moveOneFast :: FastWharf -> Int -> Int -> FastWharf
moveOneFast wharf fr to = nwharf2 where
    
    tm = head $ wharf ! fr
    nwharf1 = adjust tail fr wharf
    nwharf2 = adjust (tm:) to nwharf1
moveManyFast :: FastWharf -> Int -> Int -> Int -> FastWharf
moveManyFast swharf n fr to = nw2 where
    tm = take n $ swharf ! fr
    nw1 = adjust (drop n) fr swharf
    nw2 = adjust (tm ++) to nw1

execute9000 :: FastWharf -> [Int] -> FastWharf
--exceute9000 swharf [0,a,b] = swharf
execute9000 swharf [n,a,b] 
    | n > 0 =  execute9000 (moveOneFast swharf a b) [n-1, a, b]
    | otherwise = swharf

execute9001 :: FastWharf -> [Int] -> FastWharf
execute9001 swharf [n,a,b] = moveManyFast swharf n a b




buildIMRowSingle :: FastWharf -> (Int, Char) -> FastWharf
buildIMRowSingle swharf (snum, schar) = insertWith (flip (++)) (snum+1) [schar] swharf

buildCompleteRow :: FastWharf -> [(Int, Char)] -> FastWharf
buildCompleteRow = foldl buildIMRowSingle


parseLine :: String -> [Int]
parseLine line = mapMaybe readMaybe $ words line


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
    inp <- readFile "inputs/Day5.in"
    (stacks, insts) <- parse5
    -- let finished = foldl applyInst1 stacks insts
    -- let answer = mapMaybe safeHead finished
    -- print answer

    --let fstacks = IM.fromList $ zip [1..10] stacks
    --print fstacks
    let answer = foldl execute9000 stacks insts


    print $ getFirsts $  elems answer

-- let stacks = ["ABC", "", ""]
-- let insts1 = [[3,1,3]]

day5Part2 = do
    (stacks, insts) <- parse5
    -- let finished = foldl applyInst2 stacks insts
    -- let answer = mapMaybe safeHead finished
    -- print answer


    --let fstacks = IM.fromList $ zip [1..10] stacks

    let answer = foldl execute9001 stacks insts

    print $ getFirsts $ elems answer
day5 = solveDay day5Part1 day5Part2 5