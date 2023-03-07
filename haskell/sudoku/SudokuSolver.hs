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
getRow s r = [s (r, c) | c <- values]

freeInRow :: Sudoku -> Row -> [Value]
freeInRow s r = values \\ getRow s r

getCol :: Sudoku -> Column -> [Value]
getCol s c = [s (r, c) | r <- values]

freeInCol :: Sudoku -> Column -> [Value]
freeInCol s c = values \\ getCol s c

getCenter :: Value -> [Value]
getCenter n
   |  n `elem` [1..3] = [2]
   |  n `elem` [4..6] = [5]
   |  n `elem` [7..9] = [8]


getSubgrid :: Sudoku -> (Row, Column) -> [Value]
getSubgrid s (r, c) = [s (a + i, b + j) |a <- getCenter r, b <- getCenter c, i <- [-1..1], j <- [-1..1]]

freeInSubgrid :: Sudoku -> (Row, Column) -> [Value]
freeInSubgrid s (r, c) = values \\ getSubgrid s (r, c)


openPositions :: Sudoku -> [(Row, Column)]
openPositions s = [(r, c) | r <- values, c <- values, s (r, c) == 0]

rowValid :: Sudoku -> Row -> Bool
rowValid s r = length (getRow s r) == 9 && null (values \\ getRow s r)

colValid :: Sudoku -> Column -> Bool
colValid s r = length (getCol s r) == 9 && null (values \\ getCol s r)

subgridValid :: Sudoku -> (Row, Column) -> Bool
subgridValid s (r, c) = length (getSubgrid s (r, c)) == 9 && null (values \\ getSubgrid s (r, c))

consistent :: Sudoku -> Bool
consistent s = and [rowValid s r | r <- values] && and [colValid s c | c <- values] && and [subgridValid s (r, c) | r <- centerOfBlocks, c <- centerOfBlocks]













sud2grid :: Sudoku -> Grid
sud2grid s = [[s (r, c) | c <- positions] | r <- positions]

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
