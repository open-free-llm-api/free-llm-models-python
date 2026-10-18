"""free-llm-models CLI."""
import argparse
import json
import sys

from . import all as all_models, search, get, providers, by_provider, random as random_model, meta


def _print_table(models):
    if not models:
        print('No models found.')
        return
    print(f"{'Model':<35} {'Provider':<20} {'Tools':<6} {'JSON'}")
    print('-' * 70)
    for m in models:
        tools = 'yes' if m['supportsTools'] else '-'
        js = 'yes' if m['supportsJson'] else '-'
        print(f"{m['name']:<35} {m['provider']:<20} {tools:<6} {js}")


def cmd_list(args):
    models = all_models()
    if args.provider:
        models = by_provider(args.provider)
    models = models[:args.limit]
    if args.json:
        print(json.dumps(models, indent=2))
    else:
        _print_table(models)
        if len(models) == args.limit:
            print(f'\nShowing {args.limit}. Use --limit to see more.')


def cmd_search(args):
    models = search(args.keyword)[:20]
    if args.json:
        print(json.dumps(models, indent=2))
    else:
        _print_table(models)


def cmd_info(args):
    m = get(args.name)
    if not m:
        print('Model not found. Try: search <keyword>')
        return
    if args.json:
        print(json.dumps(m, indent=2))
        return
    print(f"""
Model:    {m['name']}
Provider: {m['provider']}
Tools:    {'yes' if m['supportsTools'] else 'no'}
JSON:     {'yes' if m['supportsJson'] else 'no'}
Released: {m['released'] or 'unknown'}

Try it free: https://freellm.net
""")


def cmd_providers(args):
    provs = providers()
    if args.json:
        print(json.dumps(provs, indent=2))
        return
    print(f"{'Provider':<25} {'Models'}")
    print('-' * 35)
    for p in provs:
        print(f"{p['name']:<25} {p['count']}")


def cmd_compare(args):
    ma, mb = get(args.model_a), get(args.model_b)
    if not ma or not mb:
        print('One or both models not found.')
        return
    if args.json:
        print(json.dumps([ma, mb], indent=2))
        return
    fields = [('Provider', 'provider'), ('Tools', 'supportsTools'),
              ('JSON mode', 'supportsJson'), ('Released', 'released')]
    print(f"{'Field':<10} {ma['name']:<30} {mb['name']}")
    print('-' * 70)
    for label, key in fields:
        va, vb = ma[key], mb[key]
        if isinstance(va, bool):
            va, vb = 'yes' if va else 'no', 'yes' if vb else 'no'
        print(f"{label:<10} {str(va or '-'):<30} {vb or '-'}")


def cmd_random(args):
    m = random_model()
    if args.json:
        print(json.dumps(m, indent=2))
        return
    print(f"\nTry this free model: {m['name']} (provider: {m['provider']})")
    print("More: https://freellm.net\n")


def main():
    parser = argparse.ArgumentParser(
        prog='free-llm-models',
        description='Query 500+ free LLM APIs. Data from https://freellm.net',
    )
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    sub = parser.add_subparsers(dest='cmd')

    p = sub.add_parser('list', help='List free models')
    p.add_argument('--provider', help='Filter by provider')
    p.add_argument('--limit', type=int, default=20)
    p.set_defaults(func=cmd_list)

    p = sub.add_parser('search', help='Search models')
    p.add_argument('keyword')
    p.set_defaults(func=cmd_search)

    p = sub.add_parser('info', help='Model details')
    p.add_argument('name')
    p.set_defaults(func=cmd_info)

    p = sub.add_parser('providers', help='List providers')
    p.set_defaults(func=cmd_providers)

    p = sub.add_parser('compare', help='Compare two models')
    p.add_argument('model_a')
    p.add_argument('model_b')
    p.set_defaults(func=cmd_compare)

    p = sub.add_parser('random', help='Random model pick')
    p.set_defaults(func=cmd_random)

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        sys.exit(0)
    args.func(args)


if __name__ == '__main__':
    main()
