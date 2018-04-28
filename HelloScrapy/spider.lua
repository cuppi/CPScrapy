function main(splash, args)
    assert(splash:go(args.url))
    splash:wait(1);
    local menuList = splash:select_all('#rootList ul li .J_ping');
    assert(menuList[args.menuIndex]:mouse_click(0, 0));
    splash:wait(0.2);
    return {
        html = splash:html(),
        png = splash:png(),
        carryData = {
            menuLength=#menuList,
            currentIndex=args.menuIndex
        }
    }
end