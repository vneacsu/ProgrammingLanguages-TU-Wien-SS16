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
openInEditor file = do
    contents <- readFile file
    runCurses $ do
        setEcho False
        w <- defaultWindow
        updateWindow w $ do
            drawString contents
            drawString "\n(press q to quit)"
        render
        waitFor w (\ev -> ev == EventCharacter 'q' || ev == EventCharacter 'Q')

waitFor :: Window -> (Event -> Bool) -> Curses ()
waitFor w p = loop where
    loop = do
        ev <- getEvent w Nothing
        case ev of
            Nothing -> loop
            Just ev' -> if p ev' then return () else loop