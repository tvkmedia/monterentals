<?php
/**
 * 404 template
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

get_header();
?>

<section class="max-w-container-max mx-auto px-gutter py-section-padding text-center">
    <h1 class="font-h1 text-h1 text-primary mb-stack-md">404</h1>
    <h2 class="font-h2 text-h2 text-primary mb-stack-md"><?php esc_html_e( 'Off the map', 'montenegrodrive' ); ?></h2>
    <p class="text-body-lg text-secondary max-w-xl mx-auto mb-stack-lg">
        <?php esc_html_e( 'The page you are looking for has taken a detour. Try one of the routes below or head back to home.', 'montenegrodrive' ); ?>
    </p>
    <div class="flex flex-wrap gap-4 justify-center">
        <a href="<?php echo esc_url( home_url( '/' ) ); ?>"
           class="bg-[#FF5722] hover:bg-[#E64A19] text-white px-8 py-3.5 rounded-lg font-label-bold transition-all">
            <?php esc_html_e( 'Back to home', 'montenegrodrive' ); ?>
        </a>
        <a href="<?php echo esc_url( home_url( '/?s=' ) ); ?>"
           class="border border-primary text-primary px-8 py-3.5 rounded-lg font-label-bold hover:bg-primary hover:text-on-primary transition-all">
            <?php esc_html_e( 'Search the site', 'montenegrodrive' ); ?>
        </a>
    </div>
</section>

<?php get_footer();
