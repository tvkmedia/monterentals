<?php
/**
 * MontenegroDrive theme functions
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit; // No direct access.
}

define( 'MONTENEGRODRIVE_VERSION', '1.0.0' );

/* ------------------------------------------------------------------ *
 *  Theme setup
 * ------------------------------------------------------------------ */
function montenegrodrive_setup() {

    // Make WordPress manage <title>.
    add_theme_support( 'title-tag' );

    // Featured images for posts and pages.
    add_theme_support( 'post-thumbnails' );

    // HTML5 markup output.
    add_theme_support(
        'html5',
        array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script' )
    );

    // Custom logo uploader.
    add_theme_support(
        'custom-logo',
        array(
            'height'      => 60,
            'width'       => 240,
            'flex-height' => true,
            'flex-width'  => true,
        )
    );

    // Block editor / wide alignments.
    add_theme_support( 'align-wide' );
    add_theme_support( 'responsive-embeds' );
    add_theme_support( 'editor-styles' );

    // Register navigation menus (used as fallback when Elementor Theme Builder isn't active).
    register_nav_menus(
        array(
            'primary' => __( 'Primary Menu', 'montenegrodrive' ),
            'footer'  => __( 'Footer Menu', 'montenegrodrive' ),
        )
    );

    // Editor color palette — these colors appear in the Gutenberg color picker
    // and Elementor will read them from theme.json fallbacks.
    add_theme_support(
        'editor-color-palette',
        array(
            array( 'name' => __( 'Adriatic Blue', 'montenegrodrive' ), 'slug' => 'primary',         'color' => '#001835' ),
            array( 'name' => __( 'Sky Blue',      'montenegrodrive' ), 'slug' => 'secondary',       'color' => '#d3e2ed' ),
            array( 'name' => __( 'Vibrant Orange','montenegrodrive' ), 'slug' => 'brand-accent',    'color' => '#FF5722' ),
            array( 'name' => __( 'Soft Background','montenegrodrive'), 'slug' => 'background',      'color' => '#f7f9fb' ),
            array( 'name' => __( 'Ink',           'montenegrodrive' ), 'slug' => 'on-surface',      'color' => '#191c1e' ),
            array( 'name' => __( 'White',         'montenegrodrive' ), 'slug' => 'white',           'color' => '#ffffff' ),
        )
    );

    // Load translation files.
    load_theme_textdomain( 'montenegrodrive', get_template_directory() . '/languages' );
}
add_action( 'after_setup_theme', 'montenegrodrive_setup' );


/* ------------------------------------------------------------------ *
 *  Enqueue scripts & styles
 * ------------------------------------------------------------------ */
function montenegrodrive_enqueue_assets() {

    // Google Fonts (Plus Jakarta Sans + Inter + Material Symbols).
    wp_enqueue_style(
        'montenegrodrive-fonts',
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap',
        array(),
        null
    );

    // Tailwind via CDN with the project config inlined.
    // For production you can swap this for a compiled stylesheet — see README.md.
    wp_enqueue_script(
        'montenegrodrive-tailwind',
        'https://cdn.tailwindcss.com/3.4.0?plugins=forms,container-queries',
        array(),
        '3.4.0',
        false
    );

    // Tailwind config — applied immediately so utility classes resolve correctly.
    $tailwind_config = montenegrodrive_get_tailwind_config_js();
    wp_add_inline_script( 'montenegrodrive-tailwind', $tailwind_config, 'after' );

    // Theme stylesheet (design tokens + base).
    wp_enqueue_style(
        'montenegrodrive-style',
        get_stylesheet_uri(),
        array( 'montenegrodrive-fonts' ),
        MONTENEGRODRIVE_VERSION
    );

    // Threaded comments helper.
    if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
        wp_enqueue_script( 'comment-reply' );
    }
}
add_action( 'wp_enqueue_scripts', 'montenegrodrive_enqueue_assets' );


/**
 * Tailwind config JS (matches the Stitch design tokens).
 * Returned as a string so wp_add_inline_script can attach it.
 */
function montenegrodrive_get_tailwind_config_js() {
    return <<<'JS'
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "secondary-container": "#d3e2ed", "on-secondary": "#ffffff", "inverse-on-surface": "#eff1f3",
        "surface-variant": "#e0e3e5", "background": "#f7f9fb", "surface-tint": "#455f87",
        "on-surface-variant": "#43474e", "secondary-fixed": "#d6e5ef", "primary-fixed-dim": "#adc8f5",
        "surface-container-low": "#f2f4f6", "surface-dim": "#d8dadc", "on-tertiary-fixed": "#2e1500",
        "on-primary-fixed": "#001b3b", "on-error": "#ffffff", "on-tertiary": "#ffffff",
        "on-tertiary-fixed-variant": "#663d16", "on-primary-container": "#7b95c0",
        "on-secondary-fixed": "#0f1d25", "tertiary-container": "#472400", "error": "#ba1a1a",
        "surface": "#f7f9fb", "on-primary-fixed-variant": "#2d476e", "outline-variant": "#c4c6cf",
        "on-surface": "#191c1e", "outline": "#74777f", "surface-container": "#eceef0",
        "surface-bright": "#f7f9fb", "on-background": "#191c1e", "tertiary": "#291300",
        "primary-fixed": "#d5e3ff", "inverse-primary": "#adc8f5", "on-tertiary-container": "#bf895b",
        "on-secondary-container": "#56656e", "surface-container-highest": "#e0e3e5",
        "surface-container-high": "#e6e8ea", "secondary": "#526069", "secondary-fixed-dim": "#bac9d3",
        "on-error-container": "#93000a", "tertiary-fixed-dim": "#f6ba88", "tertiary-fixed": "#ffdcc1",
        "primary": "#001835", "inverse-surface": "#2d3133", "on-primary": "#ffffff",
        "error-container": "#ffdad6", "primary-container": "#0f2d52",
        "surface-container-lowest": "#ffffff", "on-secondary-fixed-variant": "#3b4951",
        "brand-accent": "#FF5722"
      },
      borderRadius: { DEFAULT: "0.25rem", lg: "0.5rem", xl: "0.75rem", "2xl": "1rem", "3xl": "1.5rem", full: "9999px" },
      spacing: {
        "gutter": "24px", "margin-mobile": "16px", "stack-sm": "8px", "stack-lg": "32px",
        "container-max": "1280px", "stack-md": "16px", "section-padding": "80px"
      },
      fontFamily: {
        "body-md": ["Inter"], "body-sm": ["Inter"], "label-bold": ["Inter"],
        "h2": ["Plus Jakarta Sans"], "body-lg": ["Inter"], "h3": ["Plus Jakarta Sans"],
        "h1": ["Plus Jakarta Sans"], "price-display": ["Plus Jakarta Sans"]
      },
      fontSize: {
        "body-md": ["16px", { lineHeight: "1.5", fontWeight: "400" }],
        "body-sm": ["14px", { lineHeight: "1.5", fontWeight: "400" }],
        "label-bold": ["14px", { lineHeight: "1.2", fontWeight: "600" }],
        "h2": ["32px", { lineHeight: "1.3", fontWeight: "700" }],
        "body-lg": ["18px", { lineHeight: "1.6", fontWeight: "400" }],
        "h3": ["24px", { lineHeight: "1.4", fontWeight: "600" }],
        "h1": ["48px", { lineHeight: "1.2", letterSpacing: "-0.02em", fontWeight: "700" }],
        "price-display": ["28px", { lineHeight: "1", letterSpacing: "-0.01em", fontWeight: "700" }]
      }
    }
  }
};
JS;
}


/* ------------------------------------------------------------------ *
 *  Elementor compatibility
 * ------------------------------------------------------------------ */

/**
 * Register theme support for Elementor — so it offers Theme Builder, header/footer
 * builder, and treats this as an Elementor-aware theme.
 */
function montenegrodrive_elementor_support() {
    add_theme_support( 'elementor' );
    add_theme_support( 'elementor-pro' );
    add_theme_support( 'elementor-header-footer' );
}
add_action( 'after_setup_theme', 'montenegrodrive_elementor_support' );


/**
 * Register Elementor locations so Elementor Pro Theme Builder can target them.
 */
function montenegrodrive_register_elementor_locations( $elementor_theme_manager ) {
    $elementor_theme_manager->register_all_core_location();
}
add_action( 'elementor/theme/register_locations', 'montenegrodrive_register_elementor_locations' );


/**
 * Show a one-time admin notice telling the user to install Elementor + Pro,
 * and pointing them at the importable templates bundled with the theme.
 */
function montenegrodrive_admin_notices() {
    if ( ! current_user_can( 'manage_options' ) ) {
        return;
    }
    if ( get_user_meta( get_current_user_id(), 'montenegrodrive_dismissed_setup', true ) ) {
        return;
    }
    if ( ! did_action( 'elementor/loaded' ) ) {
        echo '<div class="notice notice-warning"><p><strong>MontenegroDrive:</strong> ';
        echo esc_html__( 'Install and activate Elementor (and Elementor Pro for full Theme Builder support) to edit pages with the visual builder.', 'montenegrodrive' );
        echo '</p></div>';
    } else {
        echo '<div class="notice notice-info is-dismissible"><p><strong>MontenegroDrive:</strong> ';
        printf(
            /* translators: %s: theme directory name */
            esc_html__( 'Import the bundled Elementor templates from %s/elementor-templates/ via Templates → Saved Templates → Import Templates.', 'montenegrodrive' ),
            '<code>' . esc_html( get_template() ) . '</code>'
        );
        echo '</p></div>';
    }
}
add_action( 'admin_notices', 'montenegrodrive_admin_notices' );


/* ------------------------------------------------------------------ *
 *  Sidebars (kept minimal; Elementor handles most layout work)
 * ------------------------------------------------------------------ */
function montenegrodrive_widgets_init() {
    register_sidebar(
        array(
            'name'          => __( 'Sidebar', 'montenegrodrive' ),
            'id'            => 'sidebar-1',
            'description'   => __( 'Default sidebar.', 'montenegrodrive' ),
            'before_widget' => '<section id="%1$s" class="widget %2$s">',
            'after_widget'  => '</section>',
            'before_title'  => '<h3 class="widget-title">',
            'after_title'   => '</h3>',
        )
    );
}
add_action( 'widgets_init', 'montenegrodrive_widgets_init' );


/* ------------------------------------------------------------------ *
 *  Body classes — used by header/footer to detect Elementor canvas
 * ------------------------------------------------------------------ */
function montenegrodrive_body_classes( $classes ) {
    if ( is_singular() && function_exists( 'elementor_theme_do_location' ) ) {
        if ( elementor_theme_do_location( 'header' ) || elementor_theme_do_location( 'footer' ) ) {
            $classes[] = 'has-elementor-theme-builder';
        }
    }
    return $classes;
}
add_filter( 'body_class', 'montenegrodrive_body_classes' );
