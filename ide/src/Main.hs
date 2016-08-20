import System.Exit
import System.Environment
import UI.NCurses

main :: IO ()
main = do
    args <- getArgs
    case length args of
        0 -> die "USAGE: ide <file path>"
        _ -> openInEditor $ head args


openInEditor :: String -> IO ()
openInEditor file = runCurses $ do
    setEcho False
    w <- defaultWindow
    updateWindow w $ do
        moveCursor 1 10
        drawString $ "Editing file: " ++ file
        moveCursor 3 10
        drawString "(press q to quit)"
        moveCursor 0 0
    render
    waitFor w (\ev -> ev == EventCharacter 'q' || ev == EventCharacter 'Q')

waitFor :: Window -> (Event -> Bool) -> Curses ()
waitFor w p = loop where
    loop = do
        ev <- getEvent w Nothing
        case ev of
            Nothing -> loop
            Just ev' -> if p ev' then return () else loop