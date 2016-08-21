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
        renderCurrentContent w contents
        dispatchEvents w

renderCurrentContent :: Window -> String -> Curses ()
renderCurrentContent w contents = do
    (nrows, ncolumns) <- screenSize
    updateWindow w $ do 
        drawString $ truncateContentToScreenSize contents nrows ncolumns
        moveCursor 0 0
    render

truncateContentToScreenSize :: String -> Integer -> Integer -> String
truncateContentToScreenSize contents nrows ncolumns = 
    concat $ map (truncateLine) $ take (fromIntegral $ nrows - 1) $ lines contents
    where
        truncateLine line = (take (fromIntegral $ ncolumns - 1) line) ++ "\n"

dispatchEvents :: Window -> Curses ()
dispatchEvents w = loop where
    loop = do
        ev <- getEvent w Nothing
        case ev of
            Nothing -> loop
            Just ev' -> do
                case ev' of
                    EventCharacter '\ESC' -> return ()
                    _ -> do
                        dispatchEditorEvent w ev'
                        loop

dispatchEditorEvent :: Window -> Event -> Curses ()
dispatchEditorEvent w ev = case ev of
    EventSpecialKey KeyUpArrow -> updateCursor w (-1) 0
    EventSpecialKey KeyRightArrow -> updateCursor w 0 1
    EventSpecialKey KeyDownArrow -> updateCursor w 1 0
    EventSpecialKey KeyLeftArrow -> updateCursor w 0 (-1)
    _ -> return ()

updateCursor :: Window -> Integer -> Integer -> Curses ()
updateCursor w rowOffset columnOffset = do
    (oldRow, oldColumn) <- getCursor w
    insideWindow <- enclosed w (oldRow + rowOffset) (oldColumn + columnOffset)
    if insideWindow then
        updateWindow w $ moveCursor (oldRow + rowOffset) (oldColumn + columnOffset)
    else 
        return ()
    render