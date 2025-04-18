# kadaie_1.py

import argparse
import gzip

from Bio import SeqIO


def main():
    parser = argparse.ArgumentParser(
        description="FASTAファイル中の短い配列の割合を計算"
    )
    parser.add_argument(
        "-i", "--input", type=str, required=True, help="入力ファイル（.gz形式のFASTA）"
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        required=True,
        help="長さのカットオフ（この値以下を短いとみなす）",
    )
    args = parser.parse_args()

    total_records = 0
    short_records = 0

    with gzip.open(args.input, mode="rt") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            total_records += 1
            if len(record.seq) <= args.length:
                short_records += 1

    if total_records > 0:
        ratio = (short_records / total_records) * 100
        print(f"全レコード数: {total_records}")
        print(f"長さ{args.length}以下のレコード数: {short_records}")
        print(f"存在比率: {ratio:.2f}%")
    else:
        print("レコードが見つかりませんでした。")


if __name__ == "__main__":
    main()
