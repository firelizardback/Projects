#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <eqp/eqp.h>
#include <eqp/eqp_def.h>

double improvePhase(double input)
{
	static double correction[19]={0,8.2,15.2,23,32.2,42.8,55,71.2,90.2,111.2,132.2,150.2,165.8,179.5,189.8,199.5,206.8,214,219.8};
	int index;
	index=(int)(input/10.0);
	if(index>17) index=17;
	return ((correction[index]+(correction[index+1]-correction[index])/10.0*(input-index*10.0)));
}
double convertPhase(double ph)
{
//	static double correction[21]={0,6.6,15.3,33.9,58.7,72.9,83.5,93.5,103.4,114.0,125.5,138.0,150.9,163.8,176.5,188.2,198.9,208.7,217.5,225.5,232.8};
//	static double correction[19]={0,9,18,28,40,52.5,67.5,85.5,105.5,126.5,139,149.5,159.5,169,176.5,184,189,196,201};
	static double correction[19]={0,8.2,15.2,23,32.2,42.8,55,71.2,90.2,111.2,132.2,150.2,165.8,179.5,189.8,199.5,206.8,214,219.8};
	double result;
	
	if(ph<0) 
	{
		cout << "phase can not be less tan zero" << endl;
		exit(0);
	}
	int i=0;
	for(i=0;ph>=correction[i];i++);
	i--;
	result=i*10+10/(correction[i+1]-correction[i])*(ph-correction[i]);
	return result;
}

main(int argc,char *argv[])
{

	char str[80],dkNumber[80]="13",kNumber[80];

	printf("Enter klystron number[%s]:",dkNumber);
	gets(str);
	if(!strcmp(str,"")) strcpy(kNumber,dkNumber);
	else strcpy(kNumber,str);

	//char smp_name[16]="CK.SVPEI1330P-C";
	char smp_name[16]="CK.SVPKI";
	strcat(smp_name,kNumber);
	strcat(smp_name,"P-C");
//	strcat(smp_name,"30P-C");
//	char eqp_name[16]="CK.WFGMKS13";
	char eqp_name[16]="CK.WFGMKS";
	strcat(eqp_name,kNumber);
//	char eqp_name2[16]="CK.COMPMKS13";
	char eqp_name2[16]="CK.COMPMKS";
	strcat(eqp_name2,kNumber);
	char oper[5];
	int res,plsOption = 0,high,high2;
	double interv,dinterv=20,start,angle;
	double startT,dstartT=2200,base,dbase=90;
	double finalT,dfinalT=6800;
	double *corPhase,*out;
	Equipment eqp,eqp2,smp;
	
	eqp = EqpCreateByName (eqp_name);
	if (eqp == NULL) 
	{ 
		printf("Error!\n"); 
		exit(1);
	}

	eqp2 = EqpCreateByName (eqp_name2);
	if (eqp2 == NULL) 
	{ 
		printf("Error!\n"); 
		exit(1);
	}

	smp = EqpCreateByName (smp_name);
	if (smp == NULL) 
	{ 
		printf("Error!\n"); exit(1);
	}

	printf("Enter interval[%f]:",dinterv);
	gets(str);
	if(!strcmp(str,"")) interv=dinterv;
	else interv=atof(str);

	printf("Enter start time[%f]:",dstartT);
	gets(str);
	if(!strcmp(str,"")) startT=dstartT;
	else startT=atof(str);

	printf("Enter final time[%f]:",dfinalT);
	gets(str);
	if(!strcmp(str,"")) finalT=dfinalT;
	else finalT=atof(str);

	printf("Enter base angle[%f]:",dbase);
	gets(str);
	if(!strcmp(str,"")) base=dbase;
	else base=atof(str);

	printf("Enter operation(Flat,Correctionfile,0):");
	gets(oper);

	high2=(finalT-startT)/interv;
	res = EqpWrite (smp, EQP_INTERV, plsOption, &interv, 1, NULL, 0);
	res = EqpRead (smp, EQP_DELAY,   plsOption, &start,  1, NULL, 0);
	res = EqpWrite (smp, EQP_STRT,   plsOption, &startT,  1, NULL, 0);
	res = EqpSetProperty (smp, EQP_HIGH, EQP_TYPE_INT, 1);
	res = EqpRead (smp, EQP_HIGH,   plsOption, &high,   1, NULL, 0);
	res = EqpRead (eqp2, EQP_CCV, plsOption, &angle, 1, NULL, 0);

	cout << high <<"  "<<high2 << endl;
	if(startT<start || high2>high)
	{
		cout << "Error in not adaption between TS and T_pulse with devices" << endl;
		exit(1);
	}
	high=high2;
	if (!(corPhase =new double[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(out =new double[high*2]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	res = EqpSetProperty (smp, EQP_AQN, EQP_TYPE_DOUBLE, high);
	res = EqpRead (smp, EQP_AQN, plsOption, corPhase, high, NULL, 0);
	FILE *fp;
	if(!strcmp(oper,"c"))
	{
		fp=fopen(argv[1],"w");
		if(fp==NULL) 
		{
			printf("Error opening file\n");
			exit(1);  /* terminate program if out of memory */
		}
		fprintf(fp,"%f  %f  %f\n",startT,finalT,interv);
	}
	for(int i=0;i<high;i++)
	{
		out[i*2]=startT+i*interv;
		//if(base>improvePhase(270) || base<=improvePhase(90))	out[i*2+1]=convertPhase(-corPhase[i]+improvePhase(base));
		//else	out[i*2+1]=convertPhase(corPhase[i]+improvePhase(base));
		if(!strcmp(oper,"0"))	out[i*2+1]=base;
		else if(!strcmp(oper,"c"))
		{
			//if(angle>=270 || angle<=90)	out[i*2+1]=corPhase[i];
			//else	out[i*2+1]=-corPhase[i];
			out[i*2+1]=corPhase[i];
		}
		else 
		{
			//if(angle>=270 || angle<=90)	out[i*2+1]=convertPhase(corPhase[i]+improvePhase(base));
			//else	out[i*2+1]=convertPhase(-corPhase[i]+improvePhase(base));
			out[i*2+1]=convertPhase(corPhase[i]*10+improvePhase(base));
			//out[i*2+1]=convertPhase(-corPhase[i]*2+improvePhase(base));
		}
		cout << out[i*2] << "   " << out[i*2+1] << endl;
		if(!strcmp(oper,"c")) fprintf(fp,"%f   %f\n",out[i*2],out[i*2+1]);
	}
	if(strcmp(oper,"c"))
	{
		res = EqpSetProperty (eqp, EQP_CCV, EQP_TYPE_DOUBLE, high*2);
  		res = EqpWrite (eqp, EQP_CCV, plsOption, out, high*2, NULL, 0);
		if (res != 0) 
		{
			printf("Set CCV property failed for %s.\n", eqp_name);
		}
	}
	if(!strcmp(oper,"c"))
	{
		fclose(fp);
	}
	delete corPhase;
	delete out;
}
