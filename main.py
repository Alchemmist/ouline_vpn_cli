from cli import create_parser, process_args


def main():
    parser = create_parser()
    args = parser.parse_args()
    process_args(args)


if __name__ == "__main__":
    main()
