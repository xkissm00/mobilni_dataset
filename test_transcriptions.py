import sys
import argparse
import decoding


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dataset-transcriptions", required=True)
    parser.add_argument("-t", "--test-transcriptions", required=True)
    args = parser.parse_args()
    return args


def load_transcriptions(path):
    transcriptions = {}

    with open(path, "r") as f:
        for line in f:
            if len(line.strip()) > 0:
                filename, transcription = line.strip().split(maxsplit=1)
                transcriptions[filename] = transcription

    return transcriptions


def print_alignment(alignment):
    bold_start = '\033[91m'
    bold_end = '\033[0m'
    missing_char = "_"

    source_transcription = "Dataset transcription: "
    target_transcription = "Manual transcription:  "

    for pair in alignment:
        source_char, target_char = pair[0], pair[1]

        if source_char != target_char:
            if source_char is None:
                source_char = missing_char

            if target_char is None:
                target_char = missing_char

            source_char = bold_start + source_char + bold_end
            target_char = bold_start + target_char + bold_end

        source_transcription += source_char
        target_transcription += target_char

    print(source_transcription)
    print(target_transcription)


def test(dataset_transcriptions, test_transcriptions):
    first = True
    distances = []
    lengths = []

    for filename in test_transcriptions:
        if filename in dataset_transcriptions:
            source = [c for c in dataset_transcriptions[filename]]
            target = [c for c in test_transcriptions[filename]]
            alignment = decoding.levenshtein_alignment(source, target)
            distance = decoding.levenshtein_distance(source, target)

            distances.append(distance)
            lengths.append(len(test_transcriptions[filename]))

            if distance > 0:
                if first:
                    first = False
                else:
                    print("--------")

                print(filename)
                print_alignment(alignment)

        else:
            print(filename, "could not be found in dataset")

    total_length = sum(lengths)
    total_distance = sum(distances)

    print()
    print("Total length:", total_length)
    print("Total distance:", total_distance)
    print("Accuracy:", float(total_length - total_distance) / total_length)


def main():
    args = parse_args()

    dataset_transcriptions = load_transcriptions(args.dataset_transcriptions)
    test_transcriptions = load_transcriptions(args.test_transcriptions)

    test(dataset_transcriptions, test_transcriptions)

    return 0


if __name__ == "__main__":
    sys.exit(main())