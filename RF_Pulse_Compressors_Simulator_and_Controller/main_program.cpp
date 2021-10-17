#include <math.h>
#include <complex.h>
#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <eqp/eqp.h>
#include <eqp/eqp_def.h>
#include "cpgplot.h"

#define ON  1
#define OFF 0

int ProcStat=OFF,signStat=OFF;
char *externalFile;
char kNumber[80];
class Input
{
	float T_pulse,T_start,T_step;
	float *kAmp,*mPhase,*cAmp,*cPhase,*corPhase,*corPhase2;
	int high,memoryStatus,res,plsOption;
	Equipment smp1,smp2,smp3,smp4,smp5;
	void delete_all()
	{
		if(memoryStatus)
		{
			delete kAmp;
			delete mPhase;
			delete cAmp;
			delete cPhase;
			delete corPhase;
			delete corPhase2;
			memoryStatus=OFF;
		}
		else	
		{
			cout << "Try to delete the memory that not alocated yet" << endl;
			exit(1);
		}
	}
	public:
	float corStart,corFinal;
	Input(float T_pulse,float T_start,float T_step);
	~Input()
	{
		delete_all();
	}
	float show_T_start()
	{
		return (T_start);		
	}
	float show_T_pulse()
	{
		return (T_pulse);
	}
	float show_T_step()
	{
		return (T_step);
	}
	int show_high()
	{
		return ((int)(T_pulse/T_step)+1);
	}
	float amplitude(float t);
	float phase(float t);
	float outAmp(float t);
	float outPhase(float t);
	float correctPhase(float t);
	void readAgain();
	void readAgain(float T_pulse,float T_start,float T_step);
	void readAgain2();
	void improvePhase(float *inputPhase);
	float Input::improvePhase(float input);
};
Input::Input(float T_pulse,float T_start,float T_step) 
{
	this->T_pulse=T_pulse;
	this->T_start=T_start;
	this->T_step=T_step;
	cout << this->T_step<<endl;
	memoryStatus=OFF;
	plsOption=0;
	readAgain(T_pulse,T_start,T_step);
	//readAgain2();
}
void Input::readAgain(float T_pulse,float T_start,float T_step)
{
	if(memoryStatus)	delete_all();
//	char smp_name1[16]="CK.SVPKI13A-C";
	char smp_name1[16]="CK.SVPKI";
	strcat(smp_name1,kNumber);
	strcat(smp_name1,"A-C");
//	char smp_name2[16]="CK.SVWFGMKS13-C";
	char smp_name2[16]="CK.SVWFGMKS";
	strcat(smp_name2,kNumber);
	strcat(smp_name2,"-C");
//	char smp_name3[16]="CK.SVPSI13A-C";
	char smp_name3[16]="CK.SVPSI";
	strcat(smp_name3,kNumber);
	strcat(smp_name3,"A-C");
	cout << smp_name3 << endl;
//	char smp_name4[16]="CK.SVPSI13P-C";
	char smp_name4[16]="CK.SVPSI";
	strcat(smp_name4,kNumber);
	strcat(smp_name4,"P-C");
	//char smp_name5[16]="CK.SAPEI1330P-C";
//	char smp_name5[16]="CK.SVPEI1330P-C";
	char smp_name5[16]="CK.SVPKI";
	strcat(smp_name5,kNumber);
//	strcat(smp_name5,"30P-C");
//	strcat(smp_name5,"05P-C");
	strcat(smp_name5,"P-C");
	double interv;
	double high1,start1,high2,start2,high3,start3,high4,start4,high5,start5;
	smp1 = EqpCreateByName (smp_name1);
	if (smp1 == NULL) 
	{ 
		printf("Error!\n"); exit(1);
	}
  	smp2 = EqpCreateByName (smp_name2);
  	if (smp2 == NULL) 
	{ 
    		printf("Error!\n"); exit(1);
	}
	smp3 = EqpCreateByName (smp_name3);
	if (smp3 == NULL) 
	{ 
		printf("Error!\n"); exit(1);
	}
  	smp4 = EqpCreateByName (smp_name4);
  	if (smp4 == NULL) 
	{ 
    		printf("Error!\n"); exit(1);
	}
  	smp5 = EqpCreateByName (smp_name5);
  	if (smp5 == NULL) 
	{ 
    		printf("Error!\n"); exit(1);
	}

  	interv=T_step;
	double startT=T_start,startT2=T_start-700;
	res = EqpWrite (smp1, EQP_INTERV, plsOption, &interv, 1, NULL, 0);
	res = EqpRead (smp1, EQP_DELAY,   plsOption, &start1,  1, NULL, 0);
	res = EqpWrite (smp1, EQP_STRT,   plsOption, &startT,  1, NULL, 0);
	res = EqpRead (smp1, EQP_HIGH,   plsOption, &high1,   1, NULL, 0);
	cout << interv << "hello" <<endl;
	printf("%4.0f data from %f every %f ns\n", high1,start1,interv);
	res = EqpWrite (smp2, EQP_INTERV, plsOption, &interv, 1, NULL, 0);
	res = EqpRead (smp2, EQP_DELAY,   plsOption, &start2,  1, NULL, 0);
	res = EqpWrite (smp2, EQP_STRT,   plsOption, &startT,  1, NULL, 0);
	res = EqpRead (smp2, EQP_HIGH,   plsOption, &high2,   1, NULL, 0);
	printf("%4.0f data from %f every %f ns\n", high2,start2,interv);
	res = EqpWrite (smp3, EQP_INTERV, plsOption, &interv, 1, NULL, 0);
	res = EqpRead (smp3, EQP_DELAY,   plsOption, &start3,  1, NULL, 0);
	res = EqpWrite (smp3, EQP_STRT,   plsOption, &startT,  1, NULL, 0);
//	res = EqpWrite (smp3, EQP_STRT,   plsOption, &startT2,  1, NULL, 0);
	res = EqpRead (smp3, EQP_HIGH,   plsOption, &high3,   1, NULL, 0);
	printf("%4.0f data from %f every %f ns\n", high3,start3,interv);
	res = EqpWrite (smp4, EQP_INTERV, plsOption, &interv, 1, NULL, 0);
	res = EqpRead (smp4, EQP_DELAY,   plsOption, &start4,  1, NULL, 0);
	res = EqpWrite (smp4, EQP_STRT,   plsOption, &startT,  1, NULL, 0);
	res = EqpRead (smp4, EQP_HIGH,   plsOption, &high4,   1, NULL, 0);
	printf("%4.0f data from %f every %f ns\n", high4,start4,interv);
	res = EqpWrite (smp5, EQP_INTERV, plsOption, &interv, 1, NULL, 0);
	res = EqpRead (smp5, EQP_DELAY,   plsOption, &start5,  1, NULL, 0);
	res = EqpWrite (smp5, EQP_STRT,   plsOption, &startT,  1, NULL, 0);
//	res = EqpWrite (smp5, EQP_STRT,   plsOption, &startT2,  1, NULL, 0);
	res = EqpRead (smp5, EQP_HIGH,   plsOption, &high5,   1, NULL, 0);
	printf("%4.0f data from %f every %f ns\n", high5,start5,interv);

	high=show_high();
	cout << high << endl;
	if(high1<high || high2<high || start1>T_start || start2>T_start || high3<high || high4<high || start3>T_start || start4>T_start||
	high5<high || start5>startT2)
	{
		cout << "Error in not adaption between TS and T_pulse with devices" << endl;
		exit(1);
	}
	if(high1<high || high2<high || start1>T_start || start2>T_start || high3<high || high4<high || start3>T_start || start4>T_start||
	high5<high || start5>T_start)
	{
		cout << "Error in not adaption between TS and T_pulse with devices" << endl;
		exit(1);
	}
	if (!(kAmp =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(mPhase =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(cAmp =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(cPhase =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(corPhase =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(corPhase2 =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	memoryStatus=ON;
	readAgain();	
}
void Input::readAgain()
{
	res = EqpSetProperty (smp1, EQP_AQN, EQP_TYPE_FLOAT, high);
	res = EqpRead (smp1, EQP_AQN, plsOption, kAmp, high, NULL, 0);
	res = EqpSetProperty (smp2, EQP_AQN, EQP_TYPE_FLOAT, high);
	res = EqpRead (smp2, EQP_AQN, plsOption, mPhase, high, NULL, 0);
	res = EqpSetProperty (smp3, EQP_AQN, EQP_TYPE_FLOAT, high);
	res = EqpRead (smp3, EQP_AQN, plsOption, cAmp, high, NULL, 0);
	res = EqpSetProperty (smp4, EQP_AQN, EQP_TYPE_FLOAT, high);
	res = EqpRead (smp4, EQP_AQN, plsOption, cPhase, high, NULL, 0);
	res = EqpSetProperty (smp5, EQP_AQN, EQP_TYPE_FLOAT, high);
	res = EqpRead (smp5, EQP_AQN, plsOption, corPhase, high, NULL, 0);
	improvePhase(mPhase);
	FILE *fp;
	fp=fopen(externalFile,"r");
	float a,b,c;
	fscanf(fp,"%f %f %f",&a,&b,&c);
	cout << a << "  "<<b << "  "<<c << endl;
	if(c!=T_step) { cout << "not match between correction file and program setting" << endl;exit(0);}
	int number=(b-a)/c+1;
	corStart=a;
	corFinal=b;
	cout << number << endl;
	for(int i=0;i<number;i++)
	{
		fscanf(fp,"%f %f",&a,&b);
		corPhase2[i]=b;
	}
	fclose(fp);
}
void Input::readAgain2()
{
	high=show_high();
	if (!(kAmp =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(mPhase =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(cAmp =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(cPhase =new float[high]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	memoryStatus=ON;
	float amp,x,Te=850;
	float t;
	float ph;
	float af=1.1;
	float T_jump=4600,T_process=4700,phi_jump=124;
	for(int i=0;i<high;i++)
	{
		t=i*T_step;
		x=t/Te;
		if (x<=1) amp=3.119*x-3.457*x*x+1.338*x*x*x;
		else if(x>1 && t<=T_pulse) amp=1;
		else amp=0;
		
		if(t<T_jump) ph=0;
		else if(t>=T_jump && t<=T_process) ph=(t-T_jump)*phi_jump/(T_process-T_jump);
		else if(t>T_process && t<=T_pulse)	ph=(exp((t-T_process)*af/(T_pulse-T_process))-1)*(180-phi_jump)/(exp(af)-1)+phi_jump;		
		else ph=180;
		kAmp[i]=amp*amp;
		mPhase[i]=ph;
	}

}

float Input::improvePhase(float input)
{
	static float correction[19]={0,8.2,15.2,23,32.2,42.8,55,71.2,90.2,111.2,132.2,150.2,165.8,179.5,189.8,199.5,206.8,214,219.8};
	int index;
	index=(int)(input/10.0);
	if(index>17) index=17;
	return ((correction[index]+(correction[index+1]-correction[index])/10.0*(input-index*10.0)));
}

void Input::improvePhase(float *inputPhase)
{
//	static float correction[21]={0,6.6,15.3,33.9,58.7,72.9,83.5,93.5,103.4,114.0,125.5,138.0,150.9,163.8,176.5,188.2,198.9,208.7,217.5,225.5,232.8};
	for(int i=0;i<high;i++)
	{
		inputPhase[i]=improvePhase(inputPhase[i]);
	}
}
float	Input::amplitude(float t)
{
	int index=(int)((t-T_start)/T_step);
	if (t<T_start)
	{
		cout << "t is less than T_start" << endl;
		exit(1);
	}
	return sqrt(kAmp[index]);
}
float Input::phase(float t)
{
//	int index=(int)((t-T_start+700)/T_step);
	//if(t<3300) t=3300;
	//if(t>6780) t=6780;
	int index=(int)((t-T_start)/T_step);
	if (t<T_start)
	{
		cout << "t is less than T_start" << endl;
		exit(1);
	}
	//return (-Phase[index]*M_PI/180);
	//return (corPhase[index]/16.6*M_PI/180);
	//return (corPhase[index]*M_PI/180);
//	if (t>corStart && t<corFinal )return ((mPhase[index]-correctPhase(t))*M_PI/180);
//	else return (mPhase[index]*M_PI/180);
	return (mPhase[index]*M_PI/180);
}
float	Input::outAmp(float t)
{
	int index=(int)((t-T_start)/T_step);
	if (t<T_start)
	{
		cout << "t is less than T_start" << endl;
		exit(1);
	}
	//return sqrt(cAmp[index]);
	return (cAmp[index]);
}
float Input::outPhase(float t)
{
	int index=(int)((t-T_start)/T_step);
	if (t<T_start)
	{
		cout << "t is less than T_start" << endl;
		exit(1);
	}
	return cPhase[index];
}
float Input::correctPhase(float t)
{
	int index=(int)((t-corStart)/T_step);
	if (t<T_start || t>corFinal)
	{
		cout << "t is less than T_start" << endl;
		exit(1);
	}
	return (corPhase2[index]);
}
class Process
{
	Input *in;
	float T_jump,T_process,T_endproc,phi_jump,t;
	float *newPhase,*cAmp,*cPhase;
	float Q0,w,tau,beta,alfa,delW;
        float_complex vcp,vc,vcn;
       	float_complex v3_begin,v3_end;
	int memoryStatus;
	
	void allocMemory();
	float_complex equation(float t);
	float_complex equation2(float t);
	float_complex equation2(float t,float ph);
        float norm(float_complex com)
        {
	  return(real(com)*real(com)+imag(com)*imag(com));
	}
        float_complex polar(float am,float te)
        {
	  return(am*float_complex(cos(te),sin(te)));
	}
	public:
	Process(Input *in,float T_jump,float T_process,float T_endproc,float phi_jump,float Q0,float beta,float w,float delW);
	~Process()
	{
		delete newPhase;
		delete cAmp;
		delete cPhase;
	}
	float	phase(float t);
	void runCheck();
	void runProcess();
	float outAmp(float t)
	{
		int index=(int)((t-in->show_T_start())/in->show_T_step());
		if (t<in->show_T_start())
		{
			cout << "t is less than T_start" << endl;
			exit(1);
		}
		return (cAmp[index]);
	}
	float outPhase()
	{
		int index=(int)((t-in->show_T_start())/in->show_T_step());
		if (t<in->show_T_start())
		{
			cout << "t is less than T_start" << endl;
			exit(1);	
		}
		return (cPhase[index]);
	}
	float deltaW();
};
Process::Process(Input *in,float T_jump,float T_process,float T_endproc,float phi_jump,float Q0,float beta,float w,float delW)
{
	this->in=in;
	this->T_jump=T_jump;
	this->T_process=T_process;
	this->T_endproc=T_endproc;
	this->phi_jump=phi_jump;
	this->Q0=Q0;
	this->beta=beta;
	this->w=w;
	this->delW=delW;
	memoryStatus=OFF;
	allocMemory();
	tau=2*Q0/(1+beta)/w;
	alfa=2*beta/(1+beta);
}
void Process::allocMemory()
{
	int phasesize = (int)((T_endproc - T_process)/in->show_T_step()  + 1.0);
	if (!(newPhase =new float[phasesize]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(cAmp =new float[in->show_high()]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
	if (!(cPhase =new float[in->show_high()]))
	{
		printf("Not enough memory to allocate buffer\n");
		exit(1);  /* terminate program if out of memory */
	}
}
void Process::runCheck()
{
	float t;
	float_complex vr;

	t=in->show_T_start();
	vcp=vc=float_complex(0,0);
	cAmp[0]=cPhase[0]=0;
	t+=in->show_T_step();
	vc=vcp+in->show_T_step()/tau*(alfa*polar(in->amplitude(t-in->show_T_step()),in->phase(t-in->show_T_step()))-vcp*(float_complex(1,0)+float_complex(0,1)*tau*delW));
	vr=vc-polar(in->amplitude(t),in->phase(t));
	cAmp[1]=norm(vr);
	cPhase[1]=arg(vr);
	t+=in->show_T_step();
	for(int i=2;t<=in->show_T_pulse()+in->show_T_start();t+=in->show_T_step(),i++)
	{
		vcn=equation(t);
		vcp=vc;
		vc=vcn;
		vr=vc-polar(in->amplitude(t),in->phase(t));
		cAmp[i]=norm(vr);
		cPhase[i]=arg(vr);
	}
}
void Process::runProcess()
{
	float nor1,nor2,normBase,t;
	float maxPh,minPh,accuracy;
	float_complex vr;

	t=in->show_T_start();
	vcp=vc=float_complex(0,0);
	cAmp[0]=cPhase[0]=0;
	t+=in->show_T_step();
	vc=vcp+in->show_T_step()/tau*(alfa*polar(in->amplitude(t-in->show_T_step()),in->phase(t-in->show_T_step()))-vcp*(float_complex(1,0)+float_complex(0,1)*tau*delW));
	vr=vc-polar(in->amplitude(t),phase(t));
	cAmp[1]=norm(vr);
	cPhase[1]=arg(vr);
	t+=in->show_T_step();
	int i;
	for(i=2;t<=T_process;t+=in->show_T_step(),i++)
	{
		vcn=equation2(t);
		vcp=vc;
		vc=vcn;
		vr=vc-polar(in->amplitude(t),phase(t));
		cAmp[i]=norm(vr);
		cPhase[i]=arg(vr);
	}
	v3_begin=vr;
	normBase=norm(vc-polar(in->amplitude(t-in->show_T_step()),phase(t-in->show_T_step())));
	for(;t<=T_endproc;t+=in->show_T_step(),i++)
	{
		//minPh=phase(t-in->show_T_step());
		minPh=phi_jump*M_PI/180;
		maxPh=M_PI;
		accuracy=(maxPh-minPh)/(T_endproc-T_process)*in->show_T_step()/20;
                nor1=norm(equation2(t,minPh)-polar(in->amplitude(t),minPh));
                nor2=norm(equation2(t,maxPh)-polar(in->amplitude(t),maxPh));
		if((nor1-normBase)*(nor2-normBase)>0) 
			if((nor1-normBase)>0)		maxPh=minPh;
			else	minPh=maxPh;
		while((maxPh-minPh)>accuracy)
		{
			maxPh=(maxPh+minPh)/2;
                        nor1=norm(equation2(t,minPh)-polar(in->amplitude(t),minPh));
                        nor2=norm(equation2(t,maxPh)-polar(in->amplitude(t),maxPh));
			if((nor1-normBase)*(nor2-normBase)>0)
			{
				maxPh=2*maxPh-minPh;
				minPh=(maxPh+minPh)/2;
			}
		}
		int index=(int)((t-T_process)/in->show_T_step());
		newPhase[index]=(minPh+maxPh)/2.0;
		vcn=equation2(t);
		vcp=vc;
		vc=vcn;
		vr=vc-polar(in->amplitude(t),phase(t));
		cAmp[i]=norm(vr);
		cPhase[i]=arg(vr);
	}	
	v3_end=vr;
	for(;t<in->show_T_pulse()+in->show_T_start();t+=in->show_T_step(),i++)
	{
		vcn=equation2(t);
		vcp=vc;
		vc=vcn;
		vr=vc-polar(in->amplitude(t),phase(t));
		cAmp[i]=norm(vr);
		cPhase[i]=arg(vr);
	}
}
float	Process::phase(float t)
{
	float ph;
	if(t<=in->show_T_start()) ph=(T_jump-in->show_T_start())*delW;
	else if(t>in->show_T_start() && t<T_jump) ph=(T_jump-t)*delW;
//	else if(t>=T_jump && t<=T_process) ph=(t-T_jump)*phi_jump/(T_process-T_jump)*M_PI/180;
	else if(t>=T_jump && t<=T_process) ph=phi_jump*M_PI/180*sin(M_PI/2.0/(T_process-T_jump)*(t-T_jump));
	else if(t>T_process && t<=T_endproc)
		ph=newPhase[(int)((t-T_process)/in->show_T_step())];
	else ph=newPhase[(int)((T_endproc-T_process)/in->show_T_step())];
//	else ph=(t-T_jump)*delW;

	return(ph);
}
float_complex Process::equation(float t)
{
	return (equation2(t,in->phase(t-in->show_T_step())));
}
float_complex Process::equation2(float t)
{
	return (equation2(t,phase(t-in->show_T_step())));
}
float_complex Process::equation2(float t,float ph)
{
	float_complex a,b,c,a2,b2,c2,result,vg,vgp,vgn;
	float w0=w-delW,h=in->show_T_step();
	float_complex ir=float_complex(1,0);
	float_complex ii=float_complex(0,1);
	
	a=ir+ii*(float)((w*w-w0*w0)*tau/(2.0*w));
	b=ir*tau-ii/w;
	c=-ii*(float)(tau/(2.0*w));
	a2=a-c*(float)(2.0/(h*h));
	b2=-b/(float)(2.0*h)+c/(float)(h*h);
	c2=b/(float)(2.0*h)+c/(float)(h*h);
	vgp=polar(in->amplitude(t-h),ph);
	vg=polar(in->amplitude(t),ph);
	vgn=polar(in->amplitude(t+h),ph);
	result=-vc*a2-vcp*b2+alfa*vg-ii*(vgn-vgp)*(float)(alfa/w/(2.0*h));
	result/=c2;
	return (result); 
//	return(vcp+2*in->show_T_step()/tau*(alfa*polar(in->amplitude(t-in->show_T_step()),ph)-vc*(float_complex(1,0)+float_complex(0,1)*tau*delW)));
}
float Process::deltaW()
{
	return (arg(v3_end)-arg(v3_begin))/(in->show_T_pulse()+in->show_T_start()-T_process);
}
class Output
{
	float *outT,*outAmp1,*outAmp2,*outWFG;
	Input *in;
	Process *proc;
	public:
	Output(Input *in,Process *proc)
	{
		this->in=in;
		this->proc=proc;
		if (!(outT =new float[in->show_high()]))
		{
			printf("Not enough memory to allocate buffer\n");
			exit(1);  /* terminate program if out of memory */
		}
		if (!(outAmp1 =new float[in->show_high()]))
		{
			printf("Not enough memory to allocate buffer\n");
			exit(1);  /* terminate program if out of memory */
		}
		if (!(outAmp2 =new float[in->show_high()]))
		{
			printf("Not enough memory to allocate buffer\n");
			exit(1);  /* terminate program if out of memory */
		}
		if (!(outWFG =new float[in->show_high()*2+2]))
		{
			printf("Not enough memory to allocate buffer\n");
			exit(1);  /* terminate program if out of memory */
		}
		read();
	}
	float convertPhase(float ph);
	void read()
	{
		int i=0;
		for(i=0;i<in->show_high();i++)
		{
			float t=in->show_T_start()+i*in->show_T_step();
			outT[i]=t;
			outAmp1[i]=in->outAmp(t);
			outAmp2[i]=proc->outAmp(t)*0.45;
			//outAmp2[i]=in->phase(t)*180.0/M_PI+35;
			if(ProcStat)
			{
				outWFG[i*2]=outT[i];
				//if(t>in->corStart && t<in->corFinal) outWFG[i*2+1]=convertPhase(proc->phase(t)*180.0/M_PI+in->correctPhase(t));
				//else outWFG[i*2+1]=convertPhase(proc->phase(t)*180.0/M_PI);
				if(!signStat)	outWFG[i*2+1]=convertPhase(proc->phase(t)*180.0/M_PI);				
				else		outWFG[i*2+1]=convertPhase(200-(proc->phase(t)*180.0/M_PI));				
			}
		}
		if(ProcStat)
		{
			outWFG[i*2]=outT[i-1]+600;
			outWFG[i*2+1]=outWFG[1];
		}
	}
	void show();
	void write();
};
void Output::show()
{
//	if (cpgopen("?") < 1)
//	{
//		cout << "Error in chart" << endl;
//		exit(1);
//	}
	if (cpgopen("/XWINDOW") < 1)
	{
		cout << "Error in chart" << endl;
		exit(1);
	}
	cpgenv(in->show_T_start(), in->show_T_pulse()+in->show_T_start(), 0, 30, 0, 0);
	//cpgpt(in->show_high(), (const float *)outT, (const float *)outAmp,9);
	cpgsci(2);
	cpgline(in->show_high(), (const float *)outT, (const float *)outAmp1);
	cpgsci(7);
	cpgline(in->show_high(), (const float *)outT, (const float *)outAmp2);
	FILE *fp;
	fp=fopen("newout.txt","w");
	for(int i=0;i<in->show_high();i++)
	{
//		if(!ProcStat)		fprintf(fp,"%f   %f   %f   %f   %f   %f   %f\n",outT[i],in->amplitude(outT[i]),in->phase(outT[i]),proc->phase(outT[i]),outWFG[i*2+1],outAmp1[i],outAmp2[i]);
//		fprintf(fp,"%f  %f\n",outT[i],in->correctPhase(outT[i]));
		if(!ProcStat)		fprintf(fp,"%f  %f\n",outT[i],in->phase(outT[i]));
		else fprintf(fp,"%f   %f   %f   %f   %f   %f\n",outT[i],in->amplitude(outT[i]),in->phase(outT[i]),proc->phase(outT[i]),outAmp1[i],outAmp2[i]);
	}
	fclose(fp);
}
float Output::convertPhase(float ph)
{
//	static float correction[21]={0,6.6,15.3,33.9,58.7,72.9,83.5,93.5,103.4,114.0,125.5,138.0,150.9,163.8,176.5,188.2,198.9,208.7,217.5,225.5,232.8};
//	static float correction[19]={0,9,18,28,40,52.5,67.5,85.5,105.5,126.5,139,149.5,159.5,169,176.5,184,189,196,201};
	static float correction[19]={0,8.2,15.2,23,32.2,42.8,55,71.2,90.2,111.2,132.2,150.2,165.8,179.5,189.8,199.5,206.8,214,219.8};
	float result;
	
	if(ph<0) 
	{
		cout << "phase can not be less tan zero" << endl;
		exit(0);
	}
	int i=0;
	//if (ph>=correction[20]) return(180);
	for(i=0;ph>=correction[i];i++);
	i--;
	result=i*10+10/(correction[i+1]-correction[i])*(ph-correction[i]);
	return result;
}
void Output::write()
{
	int res;
	int plsOption = 0;
//	char eqp_name[16] = "CK.WFGMKS13";
	char eqp_name[16] = "CK.WFGMKS";
	Equipment eqp;
	strcat(eqp_name,kNumber);

	eqp = EqpCreateByName (eqp_name);
	if (eqp == NULL) 
	{ 
		printf("Error!\n"); 
		exit(1);
	}

	res = EqpSetProperty (eqp, EQP_CCV, EQP_TYPE_FLOAT, in->show_high()*2+2);
	for(int i=0;i<=in->show_high();i++)	cout << outWFG[i*2] << "   " << outWFG[i*2+1] << endl;
  	res = EqpWrite (eqp, EQP_CCV, plsOption, outWFG, in->show_high()*2+2, NULL, 0);
	cout << "It's work" << endl;
	if (res != 0) 
	{
		printf("Set CCV property failed for %s.\n", eqp_name);
	}
}
int  main(int argc,char *argv[])
{
	float beta,f0=2.99855,Q0,delw,phi,startT,finalT;
	float dbeta=5,dQ0=187000,ddelw=133,dphi=110,dstartT=1500,dfinalT=7500;
	float sJump,dsJump=6000,fJump,dfJump=6060,fFlat,dfFlat=6800;
	char str[80],dkNumber[80]="13";
	//int WriteStat=OFF;
	
	//externalFile=argv[1];
	printf("Enter klystron number[%s]:",dkNumber);
	gets(str);
	if(!strcmp(str,"")) strcpy(kNumber,dkNumber);
	else strcpy(kNumber,str);

	printf("Enter Beta[%f]:",dbeta);
	gets(str);
	if(!strcmp(str,"")) beta=dbeta;
	else beta=atof(str);
	
	printf("Enter deltaW[%f]:",ddelw);
	gets(str);
	if(!strcmp(str,"")) delw=ddelw;
	else delw=atof(str);

	printf("Enter Q0[%f]:",dQ0);
	gets(str);
	if(!strcmp(str,"")) Q0=dQ0;
	else Q0=atof(str);

	printf("Enter ProcStatus[OFF]:");
	gets(str);
	if(!strcmp(str,"ON")) ProcStat=ON;

//	printf("Enter WriteStatus[OFF]:");
//	gets(str);
//	if(!strcmp(str,"ON")) WriteStat=ON;

	printf("Enter startT[%f]:",dstartT);
	gets(str);
	if(!strcmp(str,"")) startT=dstartT;
	else startT=atof(str);

	printf("Enter finalT[%f]:",dfinalT);
	gets(str);
	if(!strcmp(str,"")) finalT=dfinalT;
	else finalT=atof(str);

	if(ProcStat)
	{
		printf("Enter phaseJump[%f]:",dphi);
		gets(str);
		if(!strcmp(str,"")) phi=dphi;
		else phi=atof(str);

		printf("Enter startJump[%f]:",dsJump);
		gets(str);
		if(!strcmp(str,"")) sJump=dsJump;
		else sJump=atof(str);

		printf("Enter finishJump[%f]:",dfJump);
		gets(str);
		if(!strcmp(str,"")) fJump=dfJump;
		else fJump=atof(str);

		printf("Enter FinishFlatting[%f]:",dfFlat);
		gets(str);
		if(!strcmp(str,"")) fFlat=dfFlat;
		else fFlat=atof(str);

		printf("Enter SignStatus[+]:");
		gets(str);
		if(!strcmp(str,"-")) signStat=ON;

	}
	else 
	{
		phi=dphi;	
	}
	Input inp(finalT-startT,startT,20);
//	Process* proc = new Process(&inp,5800,5820,6800,phi,Q0,beta,2*M_PI*f0,delw*2*M_PI*1e-6);
	Process* proc = new Process(&inp,sJump,fJump,fFlat,phi,Q0,beta,2*M_PI*f0,delw*2*M_PI*1e-6);
	
	if(!ProcStat)	proc->runCheck();
	else		proc->runProcess();
	Output out(&inp,proc);
	if(ProcStat)	out.write();
//	if(WriteStat)	out.write();
	out.show();
	cout << proc->deltaW()<< endl;
	delete proc;
	cpgclos();
	return 0;
}
