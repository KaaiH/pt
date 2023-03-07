import System.Environment
import Data.List
import Distribution.Utils.Structured (Structure)

type Row = Int
type Column = Int
type Value = Int
type Grid = [[Value]] -- Only used to read/write from/to a file.
type Sudoku = (Row,Column) -> Value
type Constraint = (Row, Column, [Value])
type Node = (Sudoku, [Constraint])

positions :: [Int]
positions = [1..9]

values :: [Value]
values = [1..9]

blocks :: [[Int]]
blocks = [[1..3],[4..6],[7..9]]

centerOfBlocks :: [Int]
centerOfBlocks = [2, 5, 8]

getRow ::  Sudoku -> Row -> [Value]
getRow sud r = [sud (r, c) | c <- positions]

freeInRow :: Sudoku -> Row -> [Value]
freeInRow sud r = values \\ getRow sud r

getCol :: Sudoku -> Column -> [Value]
getCol sud c = [sud (r, c) | r <- positions]

freeInCol :: Sudoku -> Column -> [Value]
freeInCol sud c = values \\ getCol sud c

getCenter :: Value -> [Value]
getCenter n
   | n <= 3 = [2]
   | n <= 6 = [5]
   | n <= 9 = [8]

getSubgrid :: Sudoku -> (Row, Column) -> [Value]
getSubgrid sud (r, c) = [sud (a + i, b + j) |a <- getCenter r, b <- getCenter c, i <- [-1..1], j <- [-1..1]]

freeInSubgrid :: Sudoku -> (Row, Column) -> [Value]
freeInSubgrid sud (r, c) = values \\ getSubgrid sud (r, c)


openPositions :: Sudoku -> [(Row, Column)]
openPositions sud = [(r, c) | r <- positions, c <- positions, sud (r, c) == 0]

rowValid :: Sudoku -> Row -> Bool
rowValid sud r = length (getRow sud r) == 9 && null (values \\ getRow sud r)

colValid :: Sudoku -> Column -> Bool
colValid sud r = length (getCol sud r) == 9 && null (values \\ getCol sud r)

subgridValid :: Sudoku -> (Row, Column) -> Bool
subgridValid sud (r, c) = length (getSubgrid sud (r, c)) == 9 && null (values \\ getSubgrid sud (r, c))

consistent :: Sudoku -> Bool
consistent sud = and [rowValid sud r | r <- positions] && and [colValid sud c | c <- positions] && and [subgridValid sud (r, c) | r <- centerOfBlocks, c <- centerOfBlocks]

constraint :: Sudoku -> (Row, Column) -> Constraint
constraint sud (r, c) = (r, c, [v | v <- values, v `elem` freeInRow sud r, v `elem` freeInCol sud c, v `elem` freeInSubgrid sud (r, c)])

-- constraints sud = [constraint sud (r, c)| r <- positions, c <- positions]
constraints :: Sudoku -> [Constraint]
constraints sud = sortBy (\(_,_,a) (_,_,b) -> compare a b) [constraint sud (r, c)| (r, c) <- openPositions sud]

-- solve :: Sudoku -> Sudoku
-- sudSet sud (r, c, [v]) = sud (r, c)
-- if consistent sud 
--    tada oplossing gevonden
-- else if constraints == []
--    geen oplossing
-- else 
--    maak een node waar de waardes worden toegevoegd. 

-- if constraints sud == [] && consistent sud == False
--    geen oplossing
-- else if con













printNode :: Node -> IO()
printNode = printSudoku . fst

sud2grid :: Sudoku -> Grid
sud2grid sud = [[sud (r, c) | c <- positions] | r <- positions]

grid2sud :: Grid -> Sudoku
grid2sud gr = \(r, c) -> pos gr (r, c)
  where pos :: [[a]] -> (Row,Column) -> a
        pos gr (r, c) = (gr !! (r - 1)) !! (c - 1)

-- Extends a sudoku with a value at (row, column).
extend :: Sudoku -> (Row, Column, Value) -> Sudoku
extend sud (r, c, v) (i, j) = if r == i && c == j then v else sud (i, j)

-- Read a file-sudoku with a Grid like format into a Sudoku.
readSudoku :: String -> IO Sudoku
readSudoku filename =
    do stringGrid <- readFile filename
       return $ (grid2sud . splitStringIntoGrid) stringGrid
       where splitStringIntoGrid = map (map readint . words) . lines
             readint x = read x :: Int

{- Prints a Sudoku to the terminal by transforming it to a grid first.
   Do not modify this, or your tests will fail.
-}
printSudoku :: Sudoku -> IO ()
printSudoku = putStr . unlines . map (unwords . map show) . sud2grid

-- Helper to parse command-line arguments.
getSudokuName :: [String] -> String
getSudokuName [] = error "Filename of sudoku as first argument."
getSudokuName (x:_) = x

main :: IO ()
main =
    do args <- getArgs
       sud <- (readSudoku . getSudokuName) args
       -- TODO: Call your solver.
       printSudoku sud
