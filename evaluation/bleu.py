from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction
import nist
if __name__ == '__main__':
    count = 0
    score = 0.
    nist_score = 0.
    f = open('./v1.txt','w')
    for line in open('../../../../../home_export/wxy/mmd_output/Target_Model_v1_/terminal_output_1.txt'):
        count += 1
        if count > 5000:
            break
        if count < 5:
            continue
        if 'finished 'in line:
            continue
        if 'Test' in line:
            continue
        if 'average test loss' in line:
            continue
        f.write('-------')
        f.write('\n')
        line = line[1:-2]
        line = line.split("'\\t'")
        candidate = line[0][1:-3]
        reference = line[1][3:-1]
        f.write(str(candidate))
        f.write('\n')
        f.write(str(reference))
        f.write('\n')
        candidate = candidate.strip().split(' ')
        nist_one = nist.main(reference.strip().split(' '), candidate)
        reference = [reference.strip().split(' ')]
        smooth = SmoothingFunction()

        # print('Cumulative 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0), smoothing_function=smooth.method1))
        # print('Cumulative 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))
        # print('Cumulative 3-gram: %f' % sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))
        f.write('Cumulative 4-gram: %f' % sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25), smoothing_function=smooth.method1))
        f.write('\n')
        score += sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25), smoothing_function=smooth.method1)

        nist_score += nist_one
        f.write('nist: %f' % nist_one)
    f.write('\n')
    f.write('total_bleu:')
    f.write(str(score))
    f.write('count')
    f.write(str(count))
    f.write('avg_bleu')
    a = float(score/count)
    f.write(str(a))
    f.write('\n')
    f.write('total_nist:')
    f.write(str(nist_score))
    f.write('avg_nist')
    a = float(nist_score / count)
    f.write(str(a))
    f.close()
