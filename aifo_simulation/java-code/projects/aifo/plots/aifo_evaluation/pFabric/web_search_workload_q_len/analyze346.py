#!/usr/bin/python

# This python scripts extracts the data from the logs that we want to plot and outputs it in a format that gnuplot can
# later on represent.

# Theoretical plot number of combinations
#!/usr/bin/python
import math

if __name__ == '__main__':

########################################################################################################################

    # Mean global flow completion time vs. utilization pFabric
    lambdas = [3600, 5200, 7000, 8900, 11100, 14150, 19000]

    FCTs = [[0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0]]
    row = 0

    for x in lambdas:
        file = "temp/sppifo/sppifo_evaluation/pFabric/web_search_workload_q_len/"+str(x)+"/TOY_C30/analysis/flow_completion.statistics"
        r = open(file, 'r')
        print(r)
        lines = r.readlines()
        #print(lines)
        for i, line in enumerate(lines):
            if "less_100KB_99th_fct_ms" in line:
                FCTs[row][0]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/web_search_workload_q_len/"+str(x)+"/TOY_C40/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_99th_fct_ms" in line:
                FCTs[row][1]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/web_search_workload_q_len/"+str(x)+"/TOY_C60/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_99th_fct_ms" in line:
                FCTs[row][2]=line.split("=")[1].split("\n")[0]
                break
        r.close()
        row = row + 1


    w = open('projects/sppifo/plots/sppifo_evaluation/pFabric/web_search_workload_q_len/pFabric_less_100KB_99th_fct_ms.dat', 'w')
    w.write("#    C30    C40    C60\n")
    w.write("3600   %s    %s    %s    \n" % (FCTs[0][0], FCTs[0][1], FCTs[0][2]))
    w.write("5200   %s    %s    %s    \n" % (FCTs[1][0], FCTs[1][1], FCTs[1][2]))
    w.write("7000   %s    %s    %s    \n" % (FCTs[2][0], FCTs[2][1], FCTs[2][2]))
    w.write("8900   %s    %s    %s    \n" % (FCTs[3][0], FCTs[3][1], FCTs[3][2]))
    w.write("11100   %s    %s    %s    \n" % (FCTs[4][0], FCTs[4][1], FCTs[4][2]))
    w.write("14150   %s    %s    %s    \n" % (FCTs[5][0], FCTs[5][1], FCTs[5][2]))
    w.write("19000   %s    %s    %s    \n" % (FCTs[6][0], FCTs[6][1], FCTs[6][2]))
    w.close()


########################################################################################################################

    # Mean global flow completion time vs. utilization pFabric
    lambdas = [3600, 5200, 7000, 8900, 11100, 14150, 19000]

    FCTs = [[0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0]]
    row = 0

    for x in lambdas:
        file = "temp/sppifo/sppifo_evaluation/pFabric/web_search_workload_q_len/"+str(x)+"/TOY_C30/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_mean_fct_ms" in line:
                FCTs[row][0]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/web_search_workload_q_len/"+str(x)+"/TOY_C40/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_mean_fct_ms" in line:
                FCTs[row][1]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/web_search_workload_q_len/"+str(x)+"/TOY_C60/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "less_100KB_mean_fct_ms" in line:
                FCTs[row][2]=line.split("=")[1].split("\n")[0]
                break
        r.close()
        row = row + 1

    w = open('projects/sppifo/plots/sppifo_evaluation/pFabric/web_search_workload_q_len/pFabric_less_100KB_mean_fct_ms.dat', 'w')
    w.write("#    C30    C40    C60\n")
    w.write("3600   %s    %s    %s    \n" % (FCTs[0][0], FCTs[0][1], FCTs[0][2]))
    w.write("5200   %s    %s    %s    \n" % (FCTs[1][0], FCTs[1][1], FCTs[1][2]))
    w.write("7000   %s    %s    %s    \n" % (FCTs[2][0], FCTs[2][1], FCTs[2][2]))
    w.write("8900   %s    %s    %s    \n" % (FCTs[3][0], FCTs[3][1], FCTs[3][2]))
    w.write("11100   %s    %s    %s    \n" % (FCTs[4][0], FCTs[4][1], FCTs[4][2]))
    w.write("14150   %s    %s    %s    \n" % (FCTs[5][0], FCTs[5][1], FCTs[5][2]))
    w.write("19000   %s    %s    %s    \n" % (FCTs[6][0], FCTs[6][1], FCTs[6][2]))
    w.close()

########################################################################################################################

    # Mean global flow completion time vs. utilization pFabric
    lambdas = [3600, 5200, 7000, 8900, 11100, 14150, 19000]

    FCTs = [[0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0]]
    row = 0

    for x in lambdas:
        file = "temp/sppifo/sppifo_evaluation/pFabric/web_search_workload_q_len/"+str(x)+"/TOY_C30/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "geq_1MB_mean_fct_ms" in line:
                FCTs[row][0]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/web_search_workload_q_len/"+str(x)+"/TOY_C40/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "geq_1MB_mean_fct_ms" in line:
                FCTs[row][1]=line.split("=")[1].split("\n")[0]
                break
        r.close()

        file = "temp/sppifo/sppifo_evaluation/pFabric/web_search_workload_q_len/"+str(x)+"/TOY_C60/analysis/flow_completion.statistics"
        r = open(file, 'r')
        lines = r.readlines()
        for i, line in enumerate(lines):
            if "geq_1MB_mean_fct_ms" in line:
                FCTs[row][2]=line.split("=")[1].split("\n")[0]
                break
        r.close()
        row = row + 1

    w = open('projects/sppifo/plots/sppifo_evaluation/pFabric/web_search_workload_q_len/pFabric_geq_1MB_mean_fct_ms.dat', 'w')
    w.write("#    C30    C40    C60\n")
    w.write("3600   %s    %s    %s    \n" % (FCTs[0][0], FCTs[0][1], FCTs[0][2]))
    w.write("5200   %s    %s    %s    \n" % (FCTs[1][0], FCTs[1][1], FCTs[1][2]))
    w.write("7000   %s    %s    %s    \n" % (FCTs[2][0], FCTs[2][1], FCTs[2][2]))
    w.write("8900   %s    %s    %s    \n" % (FCTs[3][0], FCTs[3][1], FCTs[3][2]))
    w.write("11100   %s    %s    %s    \n" % (FCTs[4][0], FCTs[4][1], FCTs[4][2]))
    w.write("14150   %s    %s    %s    \n" % (FCTs[5][0], FCTs[5][1], FCTs[5][2]))
    w.write("19000   %s    %s    %s    \n" % (FCTs[6][0], FCTs[6][1], FCTs[6][2]))
    w.close()