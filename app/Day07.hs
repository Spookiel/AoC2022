module Day07 where

import Data.List
import Data.Char
import Data.Maybe
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


sumTree :: Map [String] [(Int, String)] -> Int
sumTree tree = sumTreeHelper ["d"] where

    --sumTreeHelper :: [String] -> [Int]
    sumTreeHelper cpath = [if(size == -1) then sumTreeHelper (cpath ++ [name]) else size | (size, name) <- Map.findWithDefault [] cpath tree]

parse :: String -> [Either Command LineOut]
parse s = Data.List.map parseLine $ lines s



day7Part1 = do
    inp <- readFile "inputs/day7.in"
    let parsed = parse inp


    let m = buildTree parsed []

    --print $ Map.findWithDefault [(0,"fail")] ["a"]  m
    print m
    print $ sumTree m



day7Part2 = undefined

day7 = solveDay day7Part1 day7Part2 7