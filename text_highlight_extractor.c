#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

void error(char *msg) {
	fprintf(stderr, "%s: %s\n", msg, strerror(errno));
	exit(1);
}
int main(int argc, char *argv[]) {
	pid_t pid = fork();
	int pid_status;
	if (pid == -1) {
		error("Cannot fork the process");
	} else if (!pid) { // child process
		if (execlp("python","python","kiyeok_counter.py",argv[1],NULL) == -1) {
			error("Cannot run the script");}
	}
	sleep(1);

	pid_t pid2 = fork();
	int pid_status2;
	if (pid2 == -1) {
		error("Cannot fork the process");
	} else if (!pid2) { // child process
		if (execlp("matlab","matlab","-r","-nodesktop","analyzer ./featuredata.txt;exit;",NULL) == -1) {
			error("Cannot run the script");}
	}
	sleep(7);

	pid_t pid3 = fork();
	int pid_status3;
	if (pid3 == -1) {
		error("Cannot fork the process");
	} else if (!pid3) { // child process
		if (execlp("python","python","collector.py",argv[1],NULL) == -1) {
			error("Cannot run the script");}
	}
	sleep(40);

	return 0;
}
