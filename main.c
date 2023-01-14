#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    
    
    pid_t fork_return, d_pid;
    int exit_status = -1;
    
    if ( (fork_return = fork()) < 0) {
        perror("fork error");
        exit(1);
    }
    else if (fork_return == 0) {
        printf("child: pid = %d, ppid = %d", getpid(), getppid());
    }
    else {
        d_pid = wait(&exit_status);
        printf("parent: pid = %d, d_pid = %d, exit_status = %d", getpid(), d_pid, exit_status);
    }
    printf("bye my pid id %d", getpid());
    
    
    return 0;
}
