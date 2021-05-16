//document.refresh('https://chnsoftwaredevelopers.com/classroom/Whiteboard/Whiteboard App/Style.css');
        let links = document.getElementsByTagName('link');
        for (let i = 0; i < links.length; i++) {
            if (links[i].getAttribute('rel') == 'stylesheet') {
                let href = links[i].getAttribute('href')
                    .split('?')[0];

                let newHref = href + '?version='
                    + new Date().getMilliseconds();

                links[i].setAttribute('href', newHref);
            }
        } 