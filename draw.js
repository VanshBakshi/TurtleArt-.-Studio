
const TA_PALETTE=['#ff5f6d','#ffc371','#6a82fb','#fc5c7d','#45caff','#a18cd1','#fbc2eb','#84fab0','#f6d365','#96e6a1'];
function setupCanvas(canvas){const ctx=canvas.getContext('2d');ctx.fillStyle='#0a1020';ctx.fillRect(0,0,canvas.width,canvas.height);ctx.lineCap='round';ctx.lineJoin='round';return ctx;}
function buildStrokes(kind,seed,w,h){
 const cx=w/2,cy=h/2,scale=Math.min(w,h)*.38,strokes=[];
 const add=(x1,y1,x2,y2,i,width=2)=>strokes.push({x1,y1,x2,y2,color:TA_PALETTE[(i+seed)%TA_PALETTE.length],width});
 const point=(r,a)=>[cx+Math.cos(a)*r,cy+Math.sin(a)*r];
 if(kind==='fractal'){
   function branch(x,y,ang,len,depth,i){if(depth<=0)return;let ex=x+Math.cos(ang)*len,ey=y+Math.sin(ang)*len;add(x,y,ex,ey,i,Math.max(1,depth*.55));branch(ex,ey,ang-.48,len*.72,depth-1,i+1);branch(ex,ey,ang+.48,len*.72,depth-1,i+3);}
   branch(cx,cy+scale*.75,-Math.PI/2,scale*.42,8,seed);
 } else if(kind==='nature'){
   for(let i=0;i<100;i++){let a=i*.31,r=scale*(.1+i/145),p1=point(r,a),p2=point(r+scale*.12,a+.55);add(...p1,...p2,i,2);}
   for(let i=0;i<25;i++){let x=cx-scale+i*scale*.08;add(x,cy+scale*.7,x+scale*.12,cy+scale*.42,i,2);}
 } else if(kind==='flower'||kind==='mandala'){
   for(let ring=0;ring<6;ring++){let r=scale*(.12+ring*.12);for(let k=0;k<120;k++){let a=k*Math.PI/60+ring*.13;let p1=point(r,a),p2=point(r+scale*(.10+0.035*Math.sin(a*8)),a+.12);add(...p1,...p2,k+ring*8,1.6);}}
 } else if(kind==='spiral'||kind==='math'){
   let prev=null;for(let i=0;i<950;i++){let a=i*.105,r=scale*i/950;let p=point(r,a);if(prev)add(...prev,...p,i,2.2);prev=p;}
 } else if(kind==='geometric'||kind==='festival'||kind==='advanced'){
   for(let ring=1;ring<=8;ring++){let sides=5+(ring%4),r=scale*ring/8,pts=[];for(let k=0;k<=sides;k++)pts.push(point(r,k*Math.PI*2/sides+ring*.12));for(let k=0;k<sides;k++)add(...pts[k],...pts[k+1],ring*9+k,2);}
   for(let k=0;k<120;k++){let a=k*Math.PI/60,p1=point(scale*.18,a),p2=point(scale,a+Math.PI/3);add(...p1,...p2,k,1);}
 } else {
   let prev=null;for(let i=0;i<520;i++){let a=i*.17,r=scale*(.35+.3*Math.sin(i*.04));let p=point(r,a);if(prev)add(...prev,...p,i,2);prev=p;}
 }
 return strokes;
}
function renderStrokes(canvas,strokes,count){let ctx=setupCanvas(canvas);for(let i=0;i<Math.min(count,strokes.length);i++){let s=strokes[i];ctx.strokeStyle=s.color;ctx.lineWidth=s.width;ctx.beginPath();ctx.moveTo(s.x1,s.y1);ctx.lineTo(s.x2,s.y2);ctx.stroke();}}
function previewPattern(canvas,kind,seed){let strokes=buildStrokes(kind,seed,canvas.width,canvas.height);renderStrokes(canvas,strokes,strokes.length);}
function setupStudio(id,kind,seed){
 const canvas=document.getElementById(id),strokes=buildStrokes(kind,seed,canvas.width,canvas.height);
 let progress=0,playing=false,timer=null;
 const status=document.getElementById('drawStatus'),speed=document.getElementById('speed');
 function paint(){renderStrokes(canvas,strokes,progress);if(status)status.textContent=progress>=strokes.length?'Complete':`${Math.round(progress/strokes.length*100)}% drawn`;}
 function stop(){playing=false;if(timer)clearInterval(timer);timer=null;}
 function play(){if(playing)return;playing=true;timer=setInterval(()=>{progress=Math.min(strokes.length,progress+Math.max(1,Math.floor(+speed.value*1.7)));paint();if(progress>=strokes.length)stop();},35);}
 document.getElementById('playBtn').onclick=play;
 document.getElementById('pauseBtn').onclick=stop;
 document.getElementById('restartBtn').onclick=()=>{stop();progress=0;paint();play();};
 if(speed)speed.oninput=()=>{};
 document.getElementById('copyBtn')?.addEventListener('click',copyCode);
 document.getElementById('copyBtn2')?.addEventListener('click',copyCode);
 const fav=document.getElementById('favoriteBtn');if(fav)fav.onclick=async()=>{let r=await fetch('/favorite/'+fav.dataset.id,{method:'POST'});let d=await r.json();if(d.ok)fav.textContent=d.saved?'♥ Saved':'♡ Add to favorites';};
 paint();play();
}
async function copyCode(){const el=document.getElementById('sourceCode');if(!el)return;try{await navigator.clipboard.writeText(el.innerText);this.textContent='Copied ✓';setTimeout(()=>this.textContent='Copy code',1300);}catch(e){alert('Copy is unavailable in this browser. Select the code and copy it manually.');}}
