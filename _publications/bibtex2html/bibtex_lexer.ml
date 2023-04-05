# 21 "bibtex_lexer.mll"
 

open Lexing
open Bibtex_parser

let serious = ref false    (* if we are inside a command or not *)

let brace_depth = ref 0

(*s To buffer string literals *)

let buffer = Buffer.create 8192

let reset_string_buffer () =
  Buffer.reset buffer

let store_string_char c =
  Buffer.add_char buffer c

let get_stored_string () =
  let s = Buffer.contents buffer in
  Buffer.reset buffer;
  s

let start_delim = ref ' '

let check_delim d = match !start_delim, d with
  | '{', '}' | '(', ')' -> ()
  | _ -> failwith "closing character does not match opening"


# 34 "bibtex_lexer.ml"
let __ocaml_lex_tables = {
  Lexing.lex_base =
   "\000\000\245\255\246\255\247\255\011\000\249\255\250\255\251\255\
    \252\255\253\255\016\000\005\000\018\000\044\000\050\000\056\000\
    \005\000\251\255\252\255\002\000\254\255\255\255\253\255\001\000\
    \252\255\253\255\254\255\255\255\058\000\254\255\068\000\006\000\
    \252\255\253\255\254\255\255\255";
  Lexing.lex_backtrk =
   "\255\255\255\255\255\255\255\255\007\000\255\255\255\255\255\255\
    \255\255\255\255\010\000\000\000\255\255\255\255\001\000\255\255\
    \255\255\255\255\255\255\004\000\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\000\000\255\255\
    \255\255\255\255\255\255\255\255";
  Lexing.lex_default =
   "\004\000\000\000\000\000\000\000\004\000\000\000\000\000\000\000\
    \000\000\000\000\012\000\255\255\012\000\012\000\255\255\255\255\
    \017\000\000\000\000\000\255\255\000\000\000\000\000\000\024\000\
    \000\000\000\000\000\000\000\000\030\000\000\000\030\000\034\000\
    \000\000\000\000\000\000\000\000";
  Lexing.lex_trans =
   "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\011\000\011\000\000\000\000\000\011\000\011\000\011\000\
    \000\000\000\000\011\000\000\000\255\255\255\255\000\000\000\000\
    \255\255\013\000\013\000\015\000\015\000\013\000\000\000\015\000\
    \011\000\000\000\003\000\008\000\022\000\011\000\000\000\020\000\
    \001\000\005\000\000\000\255\255\007\000\255\255\255\255\000\000\
    \013\000\000\000\015\000\255\255\255\255\013\000\013\000\255\255\
    \255\255\013\000\014\000\014\000\014\000\009\000\000\000\014\000\
    \010\000\015\000\015\000\029\000\029\000\015\000\032\000\029\000\
    \255\255\000\000\000\000\255\255\013\000\255\255\255\255\000\000\
    \000\000\255\255\014\000\000\000\255\255\000\000\000\000\000\000\
    \015\000\000\000\029\000\000\000\000\000\000\000\000\000\000\000\
    \014\000\019\000\000\000\000\000\255\255\000\000\029\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \255\255\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\006\000\027\000\005\000\026\000\000\000\
    \021\000\035\000\000\000\032\000\000\000\000\000\255\255\000\000\
    \255\255\000\000\000\000\255\255\000\000\014\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\255\255\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\014\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \002\000\025\000\000\000\000\000\000\000\018\000\033\000\000\000\
    \000\000\000\000\000\000\255\255\000\000\000\000\000\000\000\000\
    \255\255\000\000\255\255\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\255\255\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\029\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\255\255";
  Lexing.lex_check =
   "\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\000\000\000\000\255\255\255\255\000\000\011\000\011\000\
    \255\255\255\255\011\000\255\255\004\000\004\000\255\255\255\255\
    \004\000\010\000\010\000\012\000\012\000\010\000\255\255\012\000\
    \000\000\255\255\000\000\000\000\019\000\011\000\255\255\016\000\
    \000\000\000\000\255\255\004\000\000\000\004\000\004\000\255\255\
    \010\000\255\255\012\000\004\000\004\000\013\000\013\000\004\000\
    \010\000\013\000\012\000\014\000\014\000\000\000\255\255\014\000\
    \000\000\015\000\015\000\028\000\028\000\015\000\031\000\028\000\
    \004\000\255\255\255\255\004\000\013\000\030\000\030\000\255\255\
    \255\255\030\000\014\000\255\255\013\000\255\255\255\255\255\255\
    \015\000\255\255\028\000\255\255\255\255\255\255\255\255\255\255\
    \015\000\016\000\255\255\255\255\030\000\255\255\028\000\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \030\000\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\000\000\023\000\000\000\023\000\255\255\
    \016\000\031\000\255\255\031\000\255\255\255\255\004\000\255\255\
    \004\000\255\255\255\255\010\000\255\255\012\000\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\013\000\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\015\000\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \000\000\023\000\255\255\255\255\255\255\016\000\031\000\255\255\
    \255\255\255\255\255\255\004\000\255\255\255\255\255\255\255\255\
    \010\000\255\255\012\000\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\013\000\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\028\000\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\030\000";
  Lexing.lex_base_code =
   "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\002\000\007\000\000\000\009\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000";
  Lexing.lex_backtrk_code =
   "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\017\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000";
  Lexing.lex_default_code =
   "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\004\000\000\000\009\000\009\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000";
  Lexing.lex_trans_code =
   "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\001\000\001\000\014\000\014\000\001\000\000\000\014\000\
    \001\000\001\000\014\000\014\000\001\000\000\000\014\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \001\000\000\000\014\000\000\000\000\000\000\000\000\000\001\000\
    \000\000\014\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000";
  Lexing.lex_check_code =
   "\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\010\000\010\000\012\000\012\000\010\000\255\255\012\000\
    \013\000\013\000\015\000\015\000\013\000\255\255\015\000\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \010\000\255\255\012\000\255\255\255\255\255\255\255\255\013\000\
    \010\000\015\000\012\000\255\255\255\255\255\255\255\255\013\000\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \000\000\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\010\000\255\255\012\000\255\255\255\255\
    \255\255\255\255\013\000\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \010\000\255\255\012\000\255\255\255\255\255\255\255\255\013\000\
    \255\255\255\255";
  Lexing.lex_code =
   "\255\003\255\255\005\255\004\255\255\004\255\005\255\255\005\255\
    \255\000\003\001\004\002\005\255";
}

let rec token lexbuf =
  lexbuf.Lexing.lex_mem <- Array.make 6 (-1); __ocaml_lex_token_rec lexbuf 0
and __ocaml_lex_token_rec lexbuf __ocaml_lex_state =
  match Lexing.new_engine __ocaml_lex_tables __ocaml_lex_state lexbuf with
      | 0 ->
# 57 "bibtex_lexer.mll"
      ( token lexbuf )
# 238 "bibtex_lexer.ml"

  | 1 ->
let
# 59 "bibtex_lexer.mll"
                                        entry_type
# 244 "bibtex_lexer.ml"
= Lexing.sub_lexeme lexbuf lexbuf.Lexing.lex_mem.(0) lexbuf.Lexing.lex_mem.(1)
and
# 60 "bibtex_lexer.mll"
                    delim
# 249 "bibtex_lexer.ml"
= Lexing.sub_lexeme_char lexbuf lexbuf.Lexing.lex_mem.(2) in
# 61 "bibtex_lexer.mll"
       ( serious := true;
	 start_delim := delim;
	 match String.lowercase_ascii entry_type with
	   | "string" ->
	       Tabbrev
	   | "comment" ->
	       reset_string_buffer ();
               comment lexbuf;
               serious := false;
               Tcomment (get_stored_string ())
	   | "preamble" ->
	       Tpreamble
	   |  et ->
		Tentry (entry_type, key lexbuf)
       )
# 267 "bibtex_lexer.ml"

  | 2 ->
# 76 "bibtex_lexer.mll"
        ( if !serious then Tequal else token lexbuf )
# 272 "bibtex_lexer.ml"

  | 3 ->
# 77 "bibtex_lexer.mll"
        ( if !serious then Tsharp else token lexbuf )
# 277 "bibtex_lexer.ml"

  | 4 ->
# 78 "bibtex_lexer.mll"
        ( if !serious then Tcomma else token lexbuf )
# 282 "bibtex_lexer.ml"

  | 5 ->
# 79 "bibtex_lexer.mll"
        ( if !serious then begin
	    reset_string_buffer ();
	    brace lexbuf;
	    Tstring (get_stored_string ())
          end else
	    token lexbuf )
# 292 "bibtex_lexer.ml"

  | 6 ->
let
# 85 "bibtex_lexer.mll"
                   d
# 298 "bibtex_lexer.ml"
= Lexing.sub_lexeme_char lexbuf lexbuf.Lexing.lex_start_pos in
# 86 "bibtex_lexer.mll"
        ( if !serious then begin
	    check_delim d;
	    serious := false;
	    Trbrace
	  end else
	    token lexbuf )
# 307 "bibtex_lexer.ml"

  | 7 ->
# 93 "bibtex_lexer.mll"
      ( if !serious then
	  Tident (Lexing.lexeme lexbuf)
      	else
          token lexbuf )
# 315 "bibtex_lexer.ml"

  | 8 ->
# 98 "bibtex_lexer.mll"
      ( if !serious then begin
	  reset_string_buffer ();
          string lexbuf;
          Tstring (get_stored_string ())
	end else
	  token lexbuf )
# 325 "bibtex_lexer.ml"

  | 9 ->
# 104 "bibtex_lexer.mll"
        ( EOF )
# 330 "bibtex_lexer.ml"

  | 10 ->
# 105 "bibtex_lexer.mll"
        ( token lexbuf )
# 335 "bibtex_lexer.ml"

  | __ocaml_lex_state -> lexbuf.Lexing.refill_buff lexbuf;
      __ocaml_lex_token_rec lexbuf __ocaml_lex_state

and string lexbuf =
   __ocaml_lex_string_rec lexbuf 16
and __ocaml_lex_string_rec lexbuf __ocaml_lex_state =
  match Lexing.engine __ocaml_lex_tables __ocaml_lex_state lexbuf with
      | 0 ->
# 109 "bibtex_lexer.mll"
      ( store_string_char '{';
      	brace lexbuf;
	store_string_char '}';
	string lexbuf
      )
# 351 "bibtex_lexer.ml"

  | 1 ->
# 115 "bibtex_lexer.mll"
      ( () )
# 356 "bibtex_lexer.ml"

  | 2 ->
# 117 "bibtex_lexer.mll"
      ( store_string_char '\\';
        store_string_char '"';
	string lexbuf)
# 363 "bibtex_lexer.ml"

  | 3 ->
# 121 "bibtex_lexer.mll"
      ( failwith "unterminated string" )
# 368 "bibtex_lexer.ml"

  | 4 ->
# 123 "bibtex_lexer.mll"
      ( let c = Lexing.lexeme_char lexbuf 0 in
	store_string_char c;
        string lexbuf )
# 375 "bibtex_lexer.ml"

  | __ocaml_lex_state -> lexbuf.Lexing.refill_buff lexbuf;
      __ocaml_lex_string_rec lexbuf __ocaml_lex_state

and brace lexbuf =
   __ocaml_lex_brace_rec lexbuf 23
and __ocaml_lex_brace_rec lexbuf __ocaml_lex_state =
  match Lexing.engine __ocaml_lex_tables __ocaml_lex_state lexbuf with
      | 0 ->
# 129 "bibtex_lexer.mll"
      ( store_string_char '{';
      	brace lexbuf;
	store_string_char '}';
	brace lexbuf
      )
# 391 "bibtex_lexer.ml"

  | 1 ->
# 135 "bibtex_lexer.mll"
      ( () )
# 396 "bibtex_lexer.ml"

  | 2 ->
# 137 "bibtex_lexer.mll"
      ( failwith "unterminated string" )
# 401 "bibtex_lexer.ml"

  | 3 ->
# 139 "bibtex_lexer.mll"
      ( let c = Lexing.lexeme_char lexbuf 0 in
	store_string_char c;
        brace lexbuf )
# 408 "bibtex_lexer.ml"

  | __ocaml_lex_state -> lexbuf.Lexing.refill_buff lexbuf;
      __ocaml_lex_brace_rec lexbuf __ocaml_lex_state

and key lexbuf =
   __ocaml_lex_key_rec lexbuf 28
and __ocaml_lex_key_rec lexbuf __ocaml_lex_state =
  match Lexing.engine __ocaml_lex_tables __ocaml_lex_state lexbuf with
      | 0 ->
# 145 "bibtex_lexer.mll"
    ( lexeme lexbuf )
# 420 "bibtex_lexer.ml"

  | 1 ->
# 148 "bibtex_lexer.mll"
    ( raise Parsing.Parse_error )
# 425 "bibtex_lexer.ml"

  | __ocaml_lex_state -> lexbuf.Lexing.refill_buff lexbuf;
      __ocaml_lex_key_rec lexbuf __ocaml_lex_state

and comment lexbuf =
   __ocaml_lex_comment_rec lexbuf 31
and __ocaml_lex_comment_rec lexbuf __ocaml_lex_state =
  match Lexing.engine __ocaml_lex_tables __ocaml_lex_state lexbuf with
      | 0 ->
# 152 "bibtex_lexer.mll"
      ( comment lexbuf; comment lexbuf )
# 437 "bibtex_lexer.ml"

  | 1 ->
let
# 153 "bibtex_lexer.mll"
                   c
# 443 "bibtex_lexer.ml"
= Lexing.sub_lexeme_char lexbuf lexbuf.Lexing.lex_start_pos in
# 154 "bibtex_lexer.mll"
      ( store_string_char c;
        comment lexbuf )
# 448 "bibtex_lexer.ml"

  | 2 ->
# 157 "bibtex_lexer.mll"
      ( () )
# 453 "bibtex_lexer.ml"

  | 3 ->
# 159 "bibtex_lexer.mll"
      ( () )
# 458 "bibtex_lexer.ml"

  | __ocaml_lex_state -> lexbuf.Lexing.refill_buff lexbuf;
      __ocaml_lex_comment_rec lexbuf __ocaml_lex_state

;;
