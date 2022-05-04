document.addEventListener("DOMContentLoaded", function () {
    /* reStructuredText processing fixes */
    /* Move footnotes to the end of their containing section */
    let footnotes = Array.from(document.getElementsByClassName("footnote"));
    for (let element of footnotes) {
        element.closest('.entry-content,.entry-summary').append(element);
    }

    /* Fix ambiguity between skeleton and docutils "container" */
    let docutilsContainers = Array.from(document.getElementsByClassName('docutils container'));
    for (let element of docutilsContainers) {
        element.classList.remove("container");
        element.classList.add("du-container");
    }

    /* Navigation element fixes */
    /* Follow link on dropdown change */
    let navSelect = document.querySelector("nav.select select"),
        navSelectInitial = navSelect.querySelector("option.initial");
    function followNavSelect() {
        let target = this.value;
        window.location = target;
    }
    navSelect.addEventListener("change", followNavSelect);

    /* Reset nav select initial value */
    function resetNavSelect() {
        navSelect.removeEventListener("change", followNavSelect);
        navSelect.value = navSelectInitial.value;
    }
    window.addEventListener("beforeunload", resetNavSelect);


    /* Dock and undock the navigation bar on wide screens */
    let navBar = document.querySelector("nav.bar");
    function dockNavBar() {
        if (window.pageYOffset >= navBar.offsetHeight) {
            navBar.classList.add("docked");
        } else {
            navBar.classList.remove("docked");
        }
    }
    window.addEventListener("scroll", dockNavBar, { passive: true });
    window.addEventListener("resize", dockNavBar);

    /* Fix offset under nav bar on anchor link change */
    function fixOffsetNavBar() {
        if (window.pageYOffset >= navBar.offsetHeight) {
            scrollBy(0, -navBar.offsetHeight);
        }
    }
    window.addEventListener("load", fixOffsetNavBar);
    window.addEventListener("hashchange", fixOffsetNavBar);
});
