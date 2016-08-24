{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE RankNTypes #-}

module Main where

import System.Environment

import Lens.Micro
import Lens.Micro.TH

import Data.Text (pack)

import qualified Graphics.Vty as V
import qualified Brick.Widgets.Edit as E
import Brick.Widgets.Core ((<+>), (<=>), str)
import qualified Brick.Types as T
import qualified Brick.Main as M

import Brick.Util (fg)
import Brick.Markup (markup, (@?))
import Brick.AttrMap (attrMap, AttrMap)


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
  St (E.editor Editor renderContent Nothing content)

renderContent :: [String] -> T.Widget n
renderContent theLines = render theLines Odd
  where
    render [] _ = str ""
    render (l:ls) Even = renderLine l "error" <=> (render ls Odd)
    render (l:ls) Odd = renderLine l "warn" <=> (render ls Even)

    renderLine l mark = (markup $ (pack l @? mark)) <+> (str "\n")

markupMap :: AttrMap
markupMap = attrMap V.defAttr
  [ ("error",   fg V.red) 
  , ("warn",    fg V.green)
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
