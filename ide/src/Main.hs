import System.Exit
import System.Environment
import UI.NCurses

main :: IO ()
main = do
    setEnv "ESCDELAY" "25"
    args <- getArgs
    case length args of
        0 -> die "USAGE: ide <file path>"
        _ -> openInEditor $ head args


openInEditor :: String -> IO ()
openInEditor file = do
    contents <- readFile file
    runCurses $ do
        setEcho False
        w <- defaultWindow
        dispatchEvents w contents 0 0 0 0

dispatchEvents :: Window -> String -> Integer -> Integer -> Integer -> Integer -> Curses ()
dispatchEvents w contents frameRow frameCol cursorRow cursorCol = do
    renderCurrentContent w contents frameRow frameCol cursorRow cursorCol

    ev <- getEvent w Nothing
    case ev of
        Nothing -> dispatchEvents w contents frameRow frameCol cursorRow cursorCol
        Just ev' -> do
            case ev' of
                EventCharacter '\ESC' -> return ()
                EventSpecialKey KeyUpArrow -> updateCursor (cursorRow - 1) cursorCol
                EventSpecialKey KeyRightArrow -> updateCursor cursorRow (cursorCol + 1)
                EventSpecialKey KeyDownArrow -> updateCursor (cursorRow + 1) cursorCol
                EventSpecialKey KeyLeftArrow -> updateCursor cursorRow (cursorCol - 1)
                _ -> dispatchEvents w contents frameRow frameCol cursorRow cursorCol
    where
        updateCursor newRow newCol = do
            (nrows, ncols) <- screenSize

            if newRow < 0 then
                if frameRow > 0 then
                    dispatchEvents w contents (frameRow - 1) frameCol 0 newCol
                else
                    dispatchEvents w contents frameRow frameCol 0 newCol

            else if newCol < 0 then
                if frameCol > 0 then
                    dispatchEvents w contents frameRow (frameCol - 1) newRow 0
                else
                    dispatchEvents w contents frameRow frameCol newRow 0

            else if newRow >= nrows then
                dispatchEvents w contents (frameRow + 1) frameCol (nrows - 1) newCol 

            else if newCol >= ncols then
                dispatchEvents w contents frameRow (frameCol + 1) newRow (ncols - 1)

            else
                dispatchEvents w contents frameRow frameCol newRow newCol

renderCurrentContent :: Window -> String -> Integer -> Integer -> Integer -> Integer -> Curses ()
renderCurrentContent w contents frameRow frameCol cursorRow cursorCol = do
    (nrows, ncols) <- screenSize
    updateWindow w $ do 
        clear 
        drawString $ truncateContentToScreenSize contents frameRow frameCol nrows ncols
        moveCursor cursorRow cursorCol
    render

truncateContentToScreenSize :: String -> Integer -> Integer -> Integer -> Integer -> String
truncateContentToScreenSize contents row col nrows ncols = 
    concat $ map (truncateLine) getLines
    where
        getLines = take (fromIntegral $ nrows - 1) $ drop (fromIntegral row) $ lines contents
        truncateLine line = (take (fromIntegral $ ncols - 1) $ drop (fromIntegral col) line) ++ "\n"