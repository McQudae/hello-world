# src/main.py
import argparse
from typing import Any, Dict, List

from .gamma_client import GammaClient
from .clob_client import ClobClient


def cmd_list_markets(args: argparse.Namespace) -> None:
    gamma = GammaClient()
    markets = gamma.list_markets(limit=args.limit, active=not args.include_closed, closed=args.include_closed)
    print(f"Found {len(markets)} markets:")
    for m in markets:
        question = m.get("question") or m.get("title")
        slug = m.get("slug")
        token_ids = GammaClient.extract_token_ids(m)
        print(f"- {question} (slug={slug})")
        if token_ids:
            print(f"  token_ids: {', '.join(token_ids)}")


def cmd_market_by_slug(args: argparse.Namespace) -> None:
    gamma = GammaClient()
    clob = ClobClient()

    market = gamma.get_market_by_slug(args.slug)
    question = market.get("question") or market.get("title")
    print(f"Market: {question}")
    print(f"Slug:   {market.get('slug')}")
    print(f"CondID: {market.get('conditionId')}")
    token_ids = GammaClient.extract_token_ids(market)
    print(f"Token IDs: {token_ids}")

    if token_ids:
        token_id = token_ids[0]
        print(f"
Pulling order book for first token_id={token_id}...")
        book = clob.get_order_book(token_id)
        print(f"Midpoint: {book.get('midpoint')}")
        print(f"Spread:   {book.get('spread')}")
        print(f"# bids:   {len(book.get('bids', []))}")
        print(f"# asks:   {len(book.get('asks', []))}")

        print(f"
Last trade price for token_id={token_id}...")
        last = clob.get_last_trade_price(token_id)
        print(f"Price: {last.get('price')} ({last.get('side')})")
    else:
        print("No CLOB token IDs found for this market.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Polymarket barebones CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list-markets
    p_list = subparsers.add_parser("list-markets", help="List active markets")
    p_list.add_argument("--limit", type=int, default=10, help="Max number of markets to fetch")
    p_list.add_argument(
        "--include-closed",
        action="store_true",
        help="Include closed markets instead of filtering to open only",
    )
    p_list.set_defaults(func=cmd_list_markets)

    # market-by-slug
    p_slug = subparsers.add_parser("market-by-slug", help="Show details for a market slug")
    p_slug.add_argument("slug", type=str, help="Market slug from polymarket.com URL")
    p_slug.set_defaults(func=cmd_market_by_slug)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()