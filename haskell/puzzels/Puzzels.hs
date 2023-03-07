{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use map" #-}
{-# HLINT ignore "Use or" #-}
module Puzzels where

length' :: [a] -> Integer
length' = foldr (const (+ 1)) 0
-- length' = foldr (\xs -> (+) 1 ) 0

or' :: [Bool] -> Bool
or' = foldr (||) False

elem' :: Eq a => a -> [a] -> Bool
elem' x = foldr (\y acc -> (y == x) || acc) False

map' :: (a -> b) -> [a] -> [b]
map' f = foldr (\x acc -> f x : acc) []

plusplus :: [a] -> [a] -> [a]
-- plusplus xs ys = foldr (:) ys xs
plusplus = foldr (:)

reverseR :: [a] -> [a]
reverseR = foldr (\x acc -> acc ++ [x]) []

reverseL :: [a] -> [a]
reverseL = foldl (flip(:)) []

-- isPalindrome :: Eq a => [a] -> Bool
-- isPalindrome = foldr (\x acc     -> )

-- fibonacci = scanr (||) False [True, False, False, True]
-- fibonacci = scanl (\) [] [1..10]
fibonacci = 0 : scanl (+) 1 fibonacci
