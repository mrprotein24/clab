# This code is to create a sbatch submitter.sh file to make it
# easy to submit jobs on the o2 cluster 

#NOTE:  this is to create a jackhammer MSA operation only

print('Time formats are either DD-HH:MM or HH:MM:SS\n')

length=raw_input('Queue type: short (0-12:00), medium (5-00:00), long (30-00:00) ')
length='-p '+str(length)+' '
time=raw_input('Run time in DD-HH:MM or HH:MM:SS ')
time='-t '+str(time)+' '
cores =4 #default
cores='-c '+str(cores)+' '
memory=60000 #default
memory='--mem '+str(memory)+' '
#outdir='/n/groups/alquraishi/Ratul/r_02_i/parallel_universe/'


#summary='-o '+str(summary)+' '
#error='-e '+str(error)+' '

jackhammer_default="--wrap='/n/groups/alquraishi/Apps/hmmer-3.1b2-linux-intel-x86_64/binaries/jackhmmer -N 5 -Z 30000000000 --incE 1e-10 --incdomE 1e-10 -E 1e-10 --domE 1e-10 --cpu 4 "

#jacout='-o '+str(jacout)+' '
#stoout='-A '+str(stoout)+' '
#tblout='--tblout '+str(tblout)+' '

print('Sample input repo: /home/rc277/work/panacea/seqaln_feb05/human_lin.fasta\n-------------\n')
target=raw_input('Enter directory where input fastas are stored: ')

print('\nSample seq-database : /n/groups/alquraishi/Apps/databases/original_sources/soding/SRC.fasta\n-------------\n')
repo=raw_input('Enter path to seq-database: ')
reponame=raw_input('Enter reponame: ')
import os
try:
	os.mkdir('/n/groups/alquraishi/Ratul/r_02_i/parallel_universe/'+str(reponame[:3]))
except:
	pass
outdir='/n/groups/alquraishi/Ratul/r_02_i/parallel_universe/'+str(reponame[:3]+'/')

numseq=119 #hard-coded for now

aout=open('submitter'+str(reponame[:3])+'.sh','w')
for i in range(119):
	command='sbatch '+str(length)+str(time)+str(cores)+str(memory)+'-o '+str(outdir)+'summary_'
	command+=str(i+1)+'_'+str(reponame[:3])+'.txt -e '+str(outdir)+'error_'+str(i+1)+'_'+str(reponame[:3])+'.txt '
	command+=str(jackhammer_default)+'-o '+str(outdir)+'aln_'+str(i+1)+'_'+str(reponame[:3])+'.txt '
	command+='-A '+str(outdir)+'out_'+str(i+1)+'_'+str(reponame[:3])+'.sto '
	command+='--tblout '+str(outdir)+'tblout_'+str(i+1)+'_'+str(reponame[:3])+'.txt '
	command+=str(target)+str(i+1)+'.fasta '+str(repo)+str(reponame)+".fasta'"
	aout.write(str(command)+'\n\n\n')
