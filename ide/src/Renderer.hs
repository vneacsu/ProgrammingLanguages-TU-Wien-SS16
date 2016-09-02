{-# LANGUAGE OverloadedStrings #-}
module Renderer where

import qualified Graphics.Vty as V

import qualified Brick.Types as T
import Brick.Widgets.Core ((<+>), (<=>), str, emptyWidget)
import Brick.Markup (markup, (@?))
import Brick.Util (fg, bg)
import Brick.AttrMap (attrMap, AttrMap)

import Data.List.Split (splitWhen)
import Data.Text (pack)

import Text.Parsec.Error

import Lexer
import Parser

markupMap :: AttrMap
markupMap = attrMap V.defAttr
  [ ("error", bg V.red)
  , ("comment", fg V.white)
  ]

render :: String -> T.Widget n
render txt =
    let toks = tokenize txt
        tree' = parseLang toks
        
        errToks = case tree' of
            Right tree -> inspect tree
            Left err -> filter (\t -> (errorPos err) == (pos t)) toks

        tokLines = splitWhen (\t -> tokType t == NL) toks
        widgetLines = (map . map) (\t -> renderToken t errToks) tokLines
        finalLines = map mergeHoriz widgetLines
    in
        mergeVert finalLines
    where
        renderToken tok errToks =
            if isErr tok errToks then
                markup $ (pack $ text tok) @? "error"
            else if tokType tok == COMMENT then
                markup $ (pack $ text tok) @? "comment"
            else
                str $ text tok

        isErr tok errToks = (elem tok errToks) || (elem (tokType tok) [ERR_STRING])

        mergeHoriz [] = str "\n"
        mergeHoriz ws = foldl (<+>) emptyWidget ws
        
        mergeVert ws = foldl (<=>) emptyWidget ws

        inspect _ = []