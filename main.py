import argparse
from modules.stock_info_gather import StockInfo
from modules.ask_gpt import OpenAIQuestionAnswering


def main(api_key, ticker, output_file):
    # create instance of OpenAIQuestionAnswering with API key
    ai = OpenAIQuestionAnswering(api_key=api_key)

    # gather stock information using StockInfo class
    stock = StockInfo().gather_info_by_ticker(ticker)

    # create list to store results
    result = []

    # ask three different questions using OpenAIQuestionAnswering class
    # and append the answers to result list
    if stock['result'] is not None:
        for x in ai.answer_question(
            f"Faça uma análise do seguinte resultado da empresa '{stock['company_name']}': {stock['result']}"
        ).split('\n'):
            result.append(x)

    if stock['cashflow'] is not None:
        for x in ai.answer_question(
            f"Faça uma análise do seguinte resultado da empresa '{stock['company_name']}': {stock['cashflow']}"
        ).split('\n'):
            result.append(x)

    if stock['balancesheet'] is not None:
        for x in ai.answer_question(
            f"Faça uma análise do seguinte balanço patrimonial da empresa '{stock['company_name']}': {stock['balancesheet']}"
        ).split('\n'):
            result.append(x)

    # remove empty strings from result list
    result = list(filter(lambda clean: len(clean) != 0, result))

    # write results to output file if specified
    if output_file:
        with open(output_file, "a+") as f:
            for res in result:
                f.write(res)
                f.write('\n')

    # print results to console
    if len(result) == 0:
        print(stock)
    else:
        for res in result:
            print(res)


if __name__ == '__main__':
    # create command line parser
    parser = argparse.ArgumentParser(description='Analyze stock information with OpenAI')

    # add arguments to parser
    parser.add_argument('ticker', type=str, help='the stock ticker symbol')
    parser.add_argument('api_key', type=str, help='the OpenAI API key')
    parser.add_argument('--no-txt', action='store_false', help="don't write results to output file")
    parser.add_argument('--output', type=str, default='output.txt', help='the output file name')

    # parse command line arguments
    args = parser.parse_args()

    # start the script and log that it's running
    print('Starting script...')
    main(args.api_key, args.ticker, args.output if args.no_txt else None)