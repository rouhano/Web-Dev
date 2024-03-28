const header = document.querySelector("header");
const sectionOne = document.querySelector("#section2");

const sectionOneOptions = {
    rootMargin: "-200px 0px 0px 0px"
};

const sectionOneObserver = new IntersectionObserver
(function(
    entries, 
    sectionOneObserver
    ){
        entries.forEach(entry => {
            // if (!entry.isIntersecting){
            //     header.classList.add("xnav-scrolled")
            // }
            // else {
            //     header.classList.remove("xnav-scrolled")
            // }
            console.log(entry.target)
        });
    }, 

sectionOneOptions);
sectionOneObserver.observe(sectionOne);