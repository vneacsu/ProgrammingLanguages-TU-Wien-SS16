{-# LANGUAGE OverloadedStrings #-}
module Renderer where

import qualified Graphics.Vty as V

import qualified Brick.Types as T
import Brick.Widgets.Core ((<+>), (<=>), str, emptyWidget)
import Brick.Markup (markup, (@?))
import Brick.Util (bg)
import Brick.AttrMap (attrMap, AttrMap)

import Data.List.Split (splitWhen)
import Data.Text (pack)

import Lexer
import Parser

markupMap :: AttrMap
markupMap = attrMap V.defAttr
  [ ("error", bg V.red)
  ]

render :: String -> T.Widget n
render txt =
    let toks = tokenize txt
        (_, errToks) = parse toks

        tokLines = splitWhen (\t -> tokType t == NL) toks
        widgetLines = (map . map) (\t -> renderToken t errToks) tokLines
        finalLines = map mergeHoriz widgetLines
    in
        mergeVert finalLines
    where
        renderToken tok errToks =
            case elem tok errToks of
                True -> markup $ (pack $ text tok) @? "error"
                False -> str $ text tok

        mergeHoriz [] = str "\n"
        mergeHoriz ws = foldl (<+>) emptyWidget ws
        
        mergeVert ws = foldl (<=>) emptyWidget ws


--renderLines :: [String] -> T.Widget n
--renderLines theLines = renderTokens $ tokenize $ unlines theLines
-- 
--renderTokens :: [Token] -> T.Widget n
--renderTokens tokens = joinLines $ renderTokLines $ splitTokLines tokens
--  where
--    splitTokLines toks = splitOn [NL] toks
--
--    renderTokLines tokLines = map (renderTokLine) tokLines
--
--    renderTokLine [] = str "\n"
--    renderTokLine toks = foldl (<+>) emptyWidget $ map renderToken toks
--
--    joinLines [] = emptyWidget
--    joinLines (l:ls) = foldl (<=>) l ls
--
--    renderToken (ID s) = markup $ (pack s @? "id")
--    renderToken (OP c) = str [c]
--    renderToken (ERR c) = markup $ (pack [c] @? "error")
--    renderToken (WS c) = str [c]
--    renderToken EOF = str "" 
--    renderToken _ = error "Unexpected token" 