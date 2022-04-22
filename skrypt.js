var iloscZn=8;
var iloscCyfr=0;
var iloscMaleL=0;
var iloscWolnychZn=0;
var iloscDuzeL=0;
var iloscSpec=0;

function iloscZnakow(){
    iloscZn=document.getElementById("iloscZnakow").value;
    
    ustawWolne();
}

function wybCyfr(){
    iloscCyfr=document.getElementById("iloscCyfr").value;
    document.getElementById("wybCyfr").value=iloscCyfr;
    ustawWolne();
}
function wybMaleL(){
    iloscMaleL=document.getElementById("iloscMaleL").value;
    document.getElementById("wybMaleL").value=iloscMaleL;
    ustawWolne();
}
function wybDuzeL(){
    iloscDuzeL=document.getElementById("iloscDuzeL").value;
    document.getElementById("wybDuzeL").value=iloscDuzeL;
    ustawWolne();
}
function wybSpec(){
    iloscSpec=document.getElementById("iloscSpec").value;
    document.getElementById("wybSpec").value=iloscSpec;
    ustawWolne();
}
function ustawWolne(){
    iloscWolnychZn=+iloscZn-(+iloscCyfr+ +iloscMaleL+ +iloscDuzeL+ +iloscSpec);
    document.getElementById("wynik").value=iloscWolnychZn;
    document.getElementById("iloscCyfr").max=+iloscCyfr+ +iloscWolnychZn;
    document.getElementById("iloscMaleL").max=+iloscMaleL+ +iloscWolnychZn;
    document.getElementById("iloscDuzeL").max=+iloscDuzeL+ +iloscWolnychZn;
    document.getElementById("iloscSpec").max=+iloscSpec+ +iloscWolnychZn;
}
function generujHaslo(){
    let haslo='';
    const alfabetMale="abcdefghijhklmnoprstuvwxyz";
    const alfabetDuze="ABCDEFGHIJHKLMNOPRSTUVWXYZ";
    const alfabetCyfry="1234567890";
    const alfabetSpec="!@#$%^&*()_+-=";

    //losowanie malych liter
    for(let i=0;i<iloscMaleL;i++){
        haslo+=alfabetMale.charAt(Math.floor(Math.random()*alfabetMale.length));
    }

    for(let i=0;i<iloscDuzeL;i++){
        haslo+=alfabetDuze.charAt(Math.floor(Math.random()*alfabetDuze.length));
    }
    for(let i=0;i<iloscCyfr;i++){
        haslo+=alfabetCyfry.charAt(Math.floor(Math.random()*alfabetCyfry.length));
    }
    for(let i=0;i<iloscSpec;i++){
        haslo+=alfabetSpec.charAt(Math.floor(Math.random()*alfabetSpec.length));
    }
    document.getElementById("test").value=zmianaKolejnosci(haslo);
}
function zmianaKolejnosci(haslo){
    let wynik=haslo.split('');
    for(let i=0;i<wynik.length;i++){
        let los=Math.floor(Math.random()*wynik.length);
        let tmp=wynik[i];
        wynik[i]=wynik[los];
        wynik[los]=tmp;
    }
    haslo=wynik.join('');
    return haslo;
}