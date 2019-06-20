$(document).ready(function() {
    $('.js__searchInSelector').on('change', function() {
        var form = $('.quickSearchForm');
        var inputJournal = $(form.find('input[name="quickLinkJournal"]'));
        var inputYear = $(form.find('input[name="quickLinkYear"]'));
        var inputVolume = $(form.find('input[name="quickLinkVolume"]'));
        var inputIssue = $(form.find('input[name="quickLinkIssue"]'));
        var inputPage = $(form.find('input[name="quickLinkPage"]'));
        if ($(inputJournal).val()) {
            $(inputYear).removeAttr("disabled");
            $(inputVolume).removeAttr("disabled");
            if ($(inputYear).val() || $(inputVolume).val()) {
                $(inputIssue).removeAttr("disabled");
                if ($(inputIssue).val()) {
                    $(inputPage).removeAttr("disabled");
                }
            }
        }
    });
    var args = window.location.search.slice(1).split("&");
    var year;
    var volume;
    $(args).each(function(i, elm) {
        var arg = elm.split('=');
        if (arg[0] == 'year') {
            year = arg[1]
        } else if (arg[0] == 'volume') {
            volume = arg[1]
        };
    });
    if (volume) {
        var elem = $(".volume-list").find("[data-attr-vol='" + volume + "']").addClass("open");
        if (elem.length) {
            $("html, body").animate({
                scrollTop: elem.offset().top
            }, 800);
        }
    } else if (year) {
        var decades = $(".decade > h3 > .title.expander");
        var currentDecade;
        for (i = 0; i < decades.length; i++) {
            dec = $(decades[i]).data("attr-vol");
            var bot = dec.split("-")[0];
            var top = dec.split("-")[1];
            if (year == top || year == bot || (year > bot && year < top)) {
                currentDecade = dec;
                break;
            }
        }
        var elem = $(".volume-list").find("[data-attr-vol='" + currentDecade + "']").addClass("open").parent().siblings(".expandable").addClass("expandedDiv").find("[data-attr-vol='" + year + "']").addClass("open").parent().siblings(".expandable").addClass("expandedDiv");
        if (elem.length) {
            $("html, body").animate({
                scrollTop: elem.offset().top
            }, 800);
        }
    } else {
        $('.slider:first-child').addClass('opened');
    }
    $(".volume-list .expander.open").each(function() {
        $(this).siblings(".expandable").addClass("expandedDiv");
        $(this).closest(".decade").find(".title.expander").siblings(".expandable.years").addClass("expandedDiv");
        if ($(this).closest(".slider").length > 0) {
            $(this).closest(".slider").parents(".expandable").addClass("expandedDiv");
            $(this).closest(".slider").closest(".expandable.volumes").prev(".expander").addClass("open");
        } else if ($(this).parent().find(".slider").length > 0) {
            $(this).parent().find(".slider").children(".expandable").addClass("expandedDiv");
            $(this).parent().find(".slider").closest(".expandable.volumes").prev(".expander").addClass("open");
        }
    });
    $('.opener, .volume-list .expander:not(.js__noloi)').click(function(e) {
        e.preventDefault();
        $(this).closest('.slider').toggleClass('opened');
        var vol = $(this).attr("data-attr-vol");
        var url = window.location.href;
        var state_to_push = "";
        if (url.indexOf("&expanded=" + vol) > 0) {
            state_to_push = url.replace("&expanded=" + vol, "");
        } else if (url.indexOf("?expanded=" + vol) > 0) {
            state_to_push = url.replace("?expanded=" + vol, "?");
        } else {
            var connector = "";
            if (url.indexOf("?") >= 0 && url.lastIndexOf("&") < (url.length - 1) && url.lastIndexOf("?") < (url.length - 1))
                connector = "&";
            else if (url.lastIndexOf("?") < (url.length - 1) && url.lastIndexOf("&") < (url.length - 1))
                connector = "?";
            state_to_push = url + connector + "expanded=" + vol;
        }
        if (state_to_push.slice(-1) == "?")
            state_to_push = state_to_push.replace("?", "");
        state_to_push = state_to_push.replace("?&", "?");
        history.replaceState(null, null, state_to_push);
    });
    var yearQueried = $("input[data-name='yearQueried']").data('year');
    var volumeQueried = $("input[data-name='volumeQueried']").data('volume');
    if (!yearQueried || !volumeQueried) {
        $(".js_issue").each(function() {
            var elem = $(this).closest(".slider");
            if (yearQueried) {
                var currentIssueYear = $(this).data('year');
                if (yearQueried == currentIssueYear) {
                    elem.toggleClass("opened");
                    return false;
                }
            } else {
                var currentVolumeId = $(this).data("volume");
                if (volumeQueried == currentVolumeId) {
                    elem.toggleClass("opened");
                    return false;
                }
            }
        });
    } else {
        $(".js_issue").each(function() {
            var elem = $(this).closest(".slider");
            var currentYearId = $(this).data("year");
            var currentVolumeId = $(this).data("volume");
            if ((yearQueried == currentYearId) && (volumeQueried == currentVolumeId)) {
                elem.toggleClass("opened");
                return false;
            }
        });
    }
});
$(document).ready(function() {
    SearchFacetsUtil.bindFacetHandlers();
});
var SearchFacetsUtil = {
    bindFacetHandlers: function() {
        $('.facetHeader').on('click', SearchFacetsUtil.toggleFacetContainer);
        $('.expand').on('click', SearchFacetsUtil.expandNestedFacets);
        $('.showMore').on('click', SearchFacetsUtil.showMoreFacetNodesHandler);
        $('.showLess').on('click', SearchFacetsUtil.showLessFacetNodesHandler);
        $('.facet-link-container').on('click', SearchFacetsUtil.checkInputStatus);
        $('.moreFacet').on('click', SearchFacetsUtil.showMoreChildNodes);
        $('.chosen-select.facets').each(function() {
            var preventAjaxTrigger = false;
            if ($(this).hasClass("js__preventAjaxTrigger")) {
                preventAjaxTrigger = true;
            }
            var mis = $(this).magicSuggest({
                hideTrigger: 'true',
                allowFreeEntries: 'false',
                expandOnFocus: true,
                maxSelection: 1,
                placeholder: $(this).data('placeholder')
            });
            if (preventAjaxTrigger) {
                $(mis).on('selectionchange', function(e, m, selection) {
                    if (selection != undefined) {
                        window.location.href = selection[0].id;
                    }
                });
            } else {
                $(mis).on('selectionchange', function(e, m, selection) {
                    if (selection != undefined) {
                        SearchUtil.resultAjaxHandler(false, selection[0].id);
                    }
                });
            }
        });
    },
    expandNestedFacets: function() {
        $(this).siblings('.childrenFacets').slideToggle('slow');
        $(this).toggle();
        $(this).siblings('.showFacetToggler').toggle();
    },
    showMoreChildNodes: function() {},
    checkInputStatus: function() {},
    showMoreFacetNodesHandler: function(e) {
        e.preventDefault();
        $(this).siblings('.hiddenChildrenFacets').slideToggle('slow', function() {
            $(this).find('input').focus();
            $(this).find('.dropdown-menu').removeClass('ms-res-ctn-scrollable');
            $(this).find('.dropdown-menu').scrollintoview({
                duration: "1000",
                complete: function() {
                    $(this).find('.dropdown-menu').addClass('ms-res-ctn-scrollable');
                }
            });
        });
        $(this).parent().find('.hiddenChildrenFacets').find('.showLess').show();
        $(this).hide();
    },
    showLessFacetNodesHandler: function(e) {
        e.preventDefault();
        $(this).closest('.hiddenChildrenFacets').slideToggle('slow');
        $(this).closest('.facetContainer').find('.showMore').show();
    },
    toggleFacetContainer: function() {
        $(this).parent().find('.facetContainer').slideToggle("slow");
    }
};
$(document).ready(function() {
    $("body").tooltip({
        items: ".tooltipTrigger[href^='#']",
        content: function() {
            return $(this.getAttribute("href")).html();
        }
    });
});

function setUpdateAction() {
    document.getElementById("actionId").value = "addJournalBookAlert";
}

function setRemoveAction() {
    document.getElementById("actionId").value = "removeJournalBookAlert";
};