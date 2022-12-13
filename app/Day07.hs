module Day07 where

import Data.List
import Data.Char
import Data.Maybe
import Debug.Trace
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Either
import Utils


data Command = Ls | Cd String deriving (Show)

data LineOut = Dir String | File Int String deriving (Show)

parseCommand :: [String] -> Command
parseCommand args
    | length args == 3 = Cd (last args)
    | otherwise = Ls

parseLineOut :: [String] -> LineOut
parseLineOut [a,b]
    | a == "dir" = Dir $ b
    | otherwise = File (read a) b


parseLine s
    | fstr == "$" = Left $ parseCommand args
    | otherwise = Right $ parseLineOut args
    where
        args = words s
        fstr = head args

buildTree :: [Either Command LineOut] -> [String] -> Map [String] [(Int, String)]
buildTree (c:cs) cpath = case c of 
    Right (File size name) -> Map.insertWith (++) (cpath) [(size, name)] nmap
    Right (Dir name) -> Map.insertWith (++) (cpath) [(-1, name)] nmap
    Left (Cd "..") -> buildTree cs (init cpath)
    Left (Cd "/") -> buildTree cs []
    Left (Cd name) -> buildTree cs (cpath ++ [name])
    _ -> buildTree cs cpath
    where 
        nmap = buildTree cs cpath
buildTree [] cpath = Map.empty


dirSizes :: Map [String] [(Int, String)] -> [Int]
dirSizes tree = sumTree tree (<= 100000000)


sumTree :: Map [String] [(Int, String)] -> (Int -> Bool) -> [Int]
sumTree tree comp = fst $ sumTreeHelper [] where

    sumTreeHelper :: [String] -> ([Int], Int)
    sumTreeHelper cpath = (lt, dsize) 
        where 
            sss = [if(size == -1) then sumTreeHelper (cpath ++ [name]) else ([],size) | (size, name) <- Map.findWithDefault [] cpath tree]
            dsize = sum $ map snd sss
            
            lt = filter comp (dsize:(concatMap fst sss))
            

parse :: String -> [Either Command LineOut]
parse s = Data.List.map parseLine $ lines s





day7Part1 = do
    inp <- readFile "inputs/day7.in"
    let parsed = parse inp

    let comp x = x <= 100000

    let m = buildTree parsed []

    print $ sum $ sumTree m comp



day7Part2 = do
    inp <- readFile "inputs/Day7.in"
    let parsed = parse inp
    let m = buildTree parsed []

    let tsize = head $ dirSizes m
    let comp x = tsize - x <= 40000000

    print $ minimum $ sumTree m comp


day7 = solveDay day7Part1 day7Part2 7