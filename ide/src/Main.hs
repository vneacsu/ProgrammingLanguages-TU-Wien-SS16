{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE RankNTypes #-}

module Main where

import System.Environment

import Lens.Micro
import Lens.Micro.TH

import Data.Text (pack)
import Data.List.Split (splitOn)

import qualified Graphics.Vty as V
import qualified Brick.Widgets.Edit as E
import Brick.Widgets.Core ((<+>), (<=>), str, emptyWidget)
import qualified Brick.Types as T
import qualified Brick.Main as M

import Brick.Util (fg)
import Brick.Markup (markup, (@?))
import Brick.AttrMap (attrMap, AttrMap)

import Lexer

data Name = Editor
          deriving (Ord, Show, Eq)

data Parity = Even | Odd

data St =
  St { _editor :: E.Editor Name }

makeLenses ''St

drawUI :: St -> [T.Widget Name]
drawUI st = [ui]
    where
        ui = E.renderEditor True (st^.editor)

appEvent :: St -> V.Event -> T.EventM Name (T.Next St)
appEvent st (V.EvKey V.KEsc []) = M.halt st
appEvent st ev = M.continue =<< T.handleEventLensed st editor E.handleEditorEvent ev

initialState :: String -> St
initialState content = 
  St (E.editor Editor renderLines Nothing content)

renderLines :: [String] -> T.Widget n
renderLines theLines = renderTokens $ tokenize $ unlines theLines
 
renderTokens :: [Token] -> T.Widget n
renderTokens tokens = joinLines $ renderTokLines $ splitTokLines tokens
  where
    splitTokLines toks = splitOn [NL] toks

    renderTokLines tokLines = map (renderTokLine) tokLines

    renderTokLine [] = str "\n"
    renderTokLine toks = foldl (<+>) emptyWidget $ map renderToken toks

    joinLines [] = emptyWidget
    joinLines (l:ls) = foldl (<=>) l ls

    renderToken (ID s) = markup $ (pack s @? "id")
    renderToken (OP c) = str [c]
    renderToken (ERR c) = markup $ (pack [c] @? "error")
    renderToken (WS c) = str [c]
    renderToken EOF = str "" 
    renderToken _ = error "Unexpected token" 

markupMap :: AttrMap
markupMap = attrMap V.defAttr
  [ ("id",    fg V.blue)
  , ("error", fg V.red)
  ]

app :: M.App St V.Event Name
app =
    M.App { M.appDraw = drawUI
          , M.appChooseCursor = M.showFirstCursor
          , M.appHandleEvent = appEvent
          , M.appStartEvent = return
          , M.appAttrMap = const markupMap
          , M.appLiftVtyEvent = id
          }

main :: IO ()
main = do
  args <- getArgs
  content <- case length args of
    0 -> return ""
    _ -> readFile $ head args
  st <- M.defaultMain app (initialState content)
  putStrLn $ unlines $ E.getEditContents $ st^.editor
